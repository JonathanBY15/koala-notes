import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [note, setNote] = useState(null);

  useEffect(() => {
    async function fetchNote() {
      try {
        const response = await fetch('http://localhost:8000/api/notes/1');  // Ensure this endpoint is correct
        if (response.ok) {
          const data = await response.json();
          setNote(data);
        } else {
          console.error('Error fetching note:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching note:', error);
      }
    }

    fetchNote();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {note ? <h1>{note.title}</h1> : <p>Loading...</p>}
      </header>
    </div>
  );
}

export default App;



