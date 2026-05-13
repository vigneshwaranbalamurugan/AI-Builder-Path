const form = document.getElementById('input-form')
const input = document.getElementById('question')
const messages = document.getElementById('messages')

function addMessage(text, who='bot', meta=''){
  const wrap = document.createElement('div')
  wrap.className = `msg ${who==='user'?'user':''}`
  const bubble = document.createElement('div')
  bubble.className = 'bubble'
  if(meta){
    const m = document.createElement('div')
    m.className = 'meta'
    m.textContent = meta
    wrap.appendChild(m)
  }
  bubble.textContent = text
  wrap.appendChild(bubble)
  messages.appendChild(wrap)
  messages.scrollTop = messages.scrollHeight
}

form.addEventListener('submit', async (e)=>{
  e.preventDefault()
  const q = input.value.trim()
  if(!q) return
  addMessage(q, 'user')
  input.value = ''

  // placeholder while waiting
  const loading = document.createElement('div')
  loading.className = 'msg'
  loading.innerHTML = `<div class="bubble">Thinking…</div>`
  messages.appendChild(loading)
  messages.scrollTop = messages.scrollHeight

  try{
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({question: q})
    })

    const data = await res.json()
    loading.remove()

    if(res.ok){
      addMessage(data.answer, 'bot')
      if(data.sources){
        addMessage(JSON.stringify(data.sources), 'bot', 'Sources')
      }
    } else {
      addMessage(data.detail || 'Error from server', 'bot')
    }
  } catch(err){
    loading.remove()
    addMessage('Network error: ' + err.message, 'bot')
  }
})
