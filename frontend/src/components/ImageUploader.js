import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Paper, Typography } from '@mui/material';

function ImageUploader({ onUpload }) {
  const onDrop = useCallback((acceptedFiles) => {
    onUpload(acceptedFiles);
  }, [onUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, accept: {'image/*': []} });

  return (
    <Paper {...getRootProps()} sx={{ padding: 2, marginBottom: 2, textAlign: 'center' }}>
      <input {...getInputProps()} />
      {isDragActive ? (
        <Typography>Drop the images here ...</Typography>
      ) : (
        <Typography>Drag 'n' drop some images here, or click to select images</Typography>
      )}
    </Paper>
  );
}

export default ImageUploader;