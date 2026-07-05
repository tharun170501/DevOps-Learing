const express = require('express');
const app = express();
const port = 3000;
// const path = require('path');

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));

// app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.render('form', { error: null });
});

const BACKENDURL = process.env.BACKENDURL || 'http://backend:5000';
console.log('Backend URL:', BACKENDURL);

app.post('/submit', async(req, res) => {
    const { name, email } = req.body;
    try {
        const response = await fetch(`${BACKENDURL}/api/submit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email }),
        });
        if (!response.ok) {
            const data = await response.json();
            throw new Error('form',{error: data.error || 'Unknown error occurred while submitting the form.'});
        }
        res.render('success');
    }
    catch (error) {
        console.error('Error submitting form:', error);
        res.render('form', { error: 'Unable to reach backend server. Please try again later.' });
    }
});
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});