import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [note, setNote] = useState(null);

  useEffect(() => {
    // Fetch note data 1 from the API
    async function fetchNote() {
      try {
        const response = await fetch('/api/notes/1');
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
        {note ? <p>{note.content}</p> : <p>Loading...</p>}
      </header>

    </div>
  );
}

export default App;



