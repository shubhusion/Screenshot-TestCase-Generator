import React, { useState } from 'react';
import ImageUploader from './components/ImageUploader';
import TestCaseDisplay from './components/TestCaseDisplay';
import { Container, Typography, TextField, Button } from '@mui/material';
import axios from 'axios';

function App() {
  const [context, setContext] = useState('');
  const [images, setImages] = useState([]);
  const [testCases, setTestCases] = useState([]);

  const handleContextChange = (event) => {
    setContext(event.target.value);
  };

  const handleImageUpload = (uploadedImages) => {
    setImages(uploadedImages);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('context', context);
    images.forEach((image, index) => {
      formData.append('images', image);
    });

    try {
      const response = await axios.post('http://localhost:5000/generate_test_cases', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setTestCases(response.data.test_cases);
    } catch (error) {
      console.error('Error generating test cases:', error);
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom>
        Screenshot Test Case Generator
      </Typography>
      <TextField
        label="Context (Optional)"
        multiline
        rows={4}
        variant="outlined"
        fullWidth
        margin="normal"
        value={context}
        onChange={handleContextChange}
      />
      <ImageUploader onUpload={handleImageUpload} />
      <Button variant="contained" color="primary" onClick={handleSubmit} disabled={images.length === 0}>
        Describe Testing Instructions
      </Button>
      <TestCaseDisplay testCases={testCases} />
    </Container>
  );
}

export default App;