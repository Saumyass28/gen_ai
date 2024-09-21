document.getElementById('query-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const queryInput = document.getElementById('query-input').value;
    const resultsDiv = document.getElementById('results');

    fetch('http://127.0.0.1:5000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: queryInput }),
    })
    .then(response => response.json())
    .then(data => {
        resultsDiv.innerHTML = '<h3>Results:</h3>';
        data.matches.forEach(match => {
            const result = document.createElement('div');
            result.textContent = `Document ID: ${match.id}, Score: ${match.score}`;
            resultsDiv.appendChild(result);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
        resultsDiv.textContent = 'An error occurred. Please try again.';
    });
});
