import React from 'react';
import { Paper, Typography, List, ListItem, ListItemText } from '@mui/material';

function TestCaseDisplay({ testCases }) {
  if (testCases.length === 0) {
    return null;
  }

  return (
    <Paper sx={{ marginTop: 2, padding: 2 }}>
      <Typography variant="h5" gutterBottom>
        Generated Test Cases
      </Typography>
      {testCases.map((testCase, index) => (
        <Paper key={index} sx={{ marginBottom: 2, padding: 1 }}>
          <Typography variant="h6">{testCase.description}</Typography>
          <Typography variant="subtitle1">Pre-conditions:</Typography>
          <Typography>{testCase.pre_conditions}</Typography>
          <Typography variant="subtitle1">Testing Steps:</Typography>
          <List>
            {testCase.testing_steps.map((step, stepIndex) => (
              <ListItem key={stepIndex}>
                <ListItemText primary={step} />
              </ListItem>
            ))}
          </List>
          <Typography variant="subtitle1">Expected Result:</Typography>
          <Typography>{testCase.expected_result}</Typography>
        </Paper>
      ))}
    </Paper>
  );
}

export default TestCaseDisplay;