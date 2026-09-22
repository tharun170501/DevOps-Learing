const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();

app.use(cors());
app.use(express.json());


const port = process.env.PORT || 5000;

const mongoURI = process.env.MONGO_URI || 'mongodb://localhost:27017/mydatabase';

mongoose.connect(mongoURI, )
.then(() => {
    console.log('Connected to MongoDB');
}).catch((err) => {
    console.error('Error connecting to MongoDB:', err);
});

const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true
    },

    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true
    }
  },
  {
    timestamps: true
  }
);

const User = mongoose.model("User", userSchema);

app.post('/api/health', (req, res) => {
    res.status(200).json({ status: 'OK' });
});

app.post('/api/users', async(req, res) => {
    try {
        const { name, email } = req.body;

        if (!name || !email) {
            return res.status(400).json({ message: 'Name and email are required' });
        }
        const user = new User({ name, email });
        const savedUser = await user.save();

        // Here you would typically save the data to your database
        res.status(201).json({ message: 'user created successfully', user: savedUser });
    } catch (error) {
        console.error('Error submitting form:', error);
        res.status(500).json({ message: 'Error submitting form. Please try again later.' });
    }
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Server is running on port ${port}`);
});