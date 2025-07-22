
import { useState } from 'react';

export default function Home() {
  const [context, setContext] = useState('');
  const [results, setResults] = useState({});

  const handleSubmit = async () => {
    const res = await fetch('https://llm-api-backend.onrender.com/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ context }),
    });
    const data = await res.json();
    setResults(data);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>LLM API/SDK Generator</h1>
      <textarea rows={6} cols={60} onChange={(e) => setContext(e.target.value)} />
      <br />
      <button onClick={handleSubmit}>Generate</button>
      <div style={{ marginTop: 20 }}>
        <h3>OpenAPI</h3>
        <pre>{results.openapi}</pre>
        <h3>gRPC</h3>
        <pre>{results.grpc}</pre>
        <h3>SDK</h3>
        <pre>{results.sdk}</pre>
      </div>
    </div>
  );
}
