## Prompt 

Generate Dockerfiles for a simple MERN stack application.

Requirements:

1. Create separate Dockerfiles for:
   - React frontend
   - Node.js + Express backend
2. Frontend Dockerfile:
   - Use Node base image
   - Install dependencies
   - Build React app
   - Expose port 3000
3. Backend Dockerfile:
   - Use Node base image
   - Install dependencies
   - Copy project files
   - Expose port 5000
   - Start server using npm start
4. Follow Docker best practices:
   - Use lightweight base image
   - Use working directory
   - Copy only required files first
   - Add comments explaining steps
5. Keep configuration simple and production-ready.

## Chatgpt
1. Frontend Dockerfile:

```Dockerfile
# -------- Stage 1: Build React App --------
# Use lightweight Node Alpine image
FROM node:20-alpine AS build

# Set working directory inside container
WORKDIR /app

# Copy package files first (improves Docker layer caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy remaining project files
COPY . .

# Build production React bundle
RUN npm run build


# -------- Stage 2: Serve Production Build --------
# Use lightweight Node image again for serving build
FROM node:20-alpine

# Install lightweight static server
RUN npm install -g serve

# Set working directory
WORKDIR /app

# Copy only the production build from previous stage
COPY --from=build /app/build ./build

# Expose React app port
EXPOSE 3000

# Serve the production React app
CMD ["serve", "-s", "build", "-l", "3000"]
```
2. Backend Dockerfile:

```Dockerfile
# Use lightweight Node Alpine base image
FROM node:20-alpine

# Set working directory inside container
WORKDIR /app

# Copy dependency files first (better caching)
COPY package*.json ./

# Install production dependencies only
RUN npm install --omit=dev

# Copy remaining backend source code
COPY . .

# Expose backend API port
EXPOSE 5000

# Start Express server
CMD ["npm", "start"]
```

## Claude Sonnet 4.5

1. Frontend Dockerfile:

```Dockerfile
# ──────────────────────────────────────────────
# Stage 1 — Build
# Install deps & compile the React production bundle
# ──────────────────────────────────────────────
FROM node:20-alpine AS builder

# Set working directory inside the container
WORKDIR /app

# Copy dependency manifests first for better layer caching.
# npm install only reruns when these files actually change.
COPY package*.json ./

# Install ALL dependencies (including devDependencies needed for the build)
RUN npm ci

# Copy the rest of the source code
COPY . .

# Compile the production build (outputs to /app/build)
RUN npm run build

# ──────────────────────────────────────────────
# Stage 2 — Serve
# Serve the static bundle with a lightweight Nginx image.
# The final image contains NO Node.js, no source code,
# and no devDependencies — just the compiled assets.
# ──────────────────────────────────────────────
FROM nginx:1.27-alpine AS runner

# Remove the default Nginx welcome page
RUN rm -rf /usr/share/nginx/html/*

# Copy compiled React assets from the builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Optional: copy a custom Nginx config (uncomment if you have one)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# React Router / SPA fallback — redirect 404s to index.html
RUN printf 'server {\n\
    listen 3000;\n\
    root /usr/share/nginx/html;\n\
    index index.html;\n\
    location / {\n\
        try_files $uri $uri/ /index.html;\n\
    }\n\
}\n' > /etc/nginx/conf.d/default.conf

# Expose the frontend port
EXPOSE 3000

# Start Nginx in the foreground (required for Docker)
CMD ["nginx", "-g", "daemon off;"]
```

2. Backend Dockerfile:

```Dockerfile
# ──────────────────────────────────────────────
# Stage 1 — Install
# Resolve and prune dependencies in isolation
# ──────────────────────────────────────────────
FROM node:20-alpine AS deps

WORKDIR /app

# Copy dependency manifests first for better layer caching.
# npm ci only reruns when these files actually change.
COPY package*.json ./

# Install production dependencies only (no devDependencies)
RUN npm ci --omit=dev

# ──────────────────────────────────────────────
# Stage 2 — Run
# Lean runtime image — no build tools, no dev packages
# ──────────────────────────────────────────────
FROM node:20-alpine AS runner

# Create a non-root user & group for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory inside the container
WORKDIR /app

# Copy pruned node_modules from the deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy application source code
COPY . .

# Give the non-root user ownership of the app directory
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose the backend API port
EXPOSE 5000

# Start the Express server.
# Using "node" directly instead of "npm start" ensures SIGTERM
# is forwarded to the process, enabling graceful shutdown.
CMD ["node", "server.js"]
```

3. Dockercompose.yml 
```yaml
version: "3.9"

services:
  # ── MongoDB ─────────────────────────────────
  mongo:
    image: mongo:7-jammy
    container_name: mern_mongo
    restart: unless-stopped
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER:-root}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD:-secret}
      MONGO_INITDB_DATABASE: ${MONGO_DB:-merndb}
    volumes:
      - mongo_data:/data/db
    networks:
      - mern_net

  # ── Express Backend ──────────────────────────
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: mern_backend
    restart: unless-stopped
    environment:
      NODE_ENV: production
      PORT: 5000
      MONGO_URI: mongodb://${MONGO_USER:-root}:${MONGO_PASSWORD:-secret}@mongo:27017/${MONGO_DB:-merndb}?authSource=admin
    ports:
      - "5000:5000"
    depends_on:
      - mongo
    networks:
      - mern_net

  # ── React Frontend ───────────────────────────
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: mern_frontend
    restart: unless-stopped
    ports:
      - "3000:3000"
    depends_on:
      - backend
    networks:
      - mern_net

volumes:
  mongo_data:

networks:
  mern_net:
    driver: bridge
```

4. .dockerignore
```dockerignore
# Dependencies — reinstalled inside the container
node_modules

# Version control
.git
.gitignore

# Local environment files — never bake secrets into images
.env
.env.*
!.env.example

# Build artefacts
build
dist
.next
out

# Logs
*.log
npm-debug.log*

# OS noise
.DS_Store
Thumbs.db

# Editor config
.vscode
.idea
*.swp

# Test files — not needed at runtime
**/__tests__
**/*.test.*
**/*.spec.*
coverage
```

## Gemini-flash-1.5
1. Backend Dockerfile
```dockerfile
# Use a lightweight Node.js image
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package files first to leverage Docker cache
COPY package*.json ./

# Install production dependencies
RUN npm install --only=production

# Copy the rest of the application source code
COPY . .

# Express typically runs on 5000; expose it
EXPOSE 5000

# Start the server
CMD ["npm", "start"]
```

2. Frontend dockerfile
```dockerfile
# --- Stage 1: Build Stage ---
FROM node:20-alpine AS build-stage

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy source and build the app
COPY . .
RUN npm run build

# --- Stage 2: Production Stage ---
# Use Nginx to serve the static production build
FROM nginx:stable-alpine

# Copy the build output from Stage 1 to Nginx's default public folder
COPY --from=build-stage /app/build /usr/share/nginx/html

# Expose port 80 (Standard for Nginx) 
# Note: You can map this to 3000 in your docker-compose or run command
EXPOSE 80

# Nginx starts automatically, no CMD needed for the default image
```

3. docker-compose.yaml

```dockerfile
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - MONGO_URI=mongodb://mongo:27017/mydb
  
  frontend:
    build: ./frontend
    ports:
      - "3000:80" # Maps local port 3000 to Nginx port 80
```

## Deepseek R1 1.5b(Local)

1. Frontend Dockerfile

```dockerfile
# Use lightweight Node.js LTS image (alpine variant)
FROM node:lts-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency files first for better caching
COPY package*.json ./

# Install production dependencies (non-dev)
RUN npm ci --only=production

# Copy all source files
COPY . .

# Build React app for production
RUN npm run build

# --- Production Stage ---
FROM node:lts-alpine

# Install static file server
RUN npm install -g serve

WORKDIR /app

# Copy build artifacts from builder stage
COPY --from=builder /app/build ./build

# Expose port 3000
EXPOSE 3000

# Serve static files
CMD ["serve", "-s", "build", "-l", "3000"]
```

2. Backend dockerfile
```dockerfile
# Use lightweight Node.js LTS image
FROM node:lts-alpine

# Set working directory
WORKDIR /app

# Copy dependency files first
COPY package*.json ./

# Install production dependencies (exclude dev dependencies)
RUN npm ci --only=production

# Copy application source
COPY . .

# Expose backend port
EXPOSE 5000

# Start Node.js server
CMD ["npm", "start"]
```
