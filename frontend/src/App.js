import React, { useState, useEffect } from 'react'

function App() {

  const [tables, setTables] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("/sakila").then(
      res => res.json()
    ).then(
      data => {
        if (data.error) {
          console.error("Error fetching data:", data.error)
        } else {
          setTables(data.tables)
        }
        setLoading(false)
      }
    )    
  }, [])


  
  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {tables.map((table, i) => (
            <li key={i}>{table}</li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default App
