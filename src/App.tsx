import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [currentTime, setCurrentTime] = useState(0)

  useEffect(() => {
    fetch('/api/time').then((res) => res.json()).then((data) => {
      setCurrentTime(data)
    })
  }, [])

  return (
    <>
    <div>
    {currentTime.time}
    </div>
    </>
  )
}

export default App
