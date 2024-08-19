import React from 'react';
import { Alert, Snackbar } from '@mui/material';

const Notification = (props) => {
  const { open, handleClose, msg, severity } = props;
  return (
    <Snackbar
      open={open}
      autoHideDuration={6000}
      onClose={handleClose}
      anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
    >
      <Alert onClose={handleClose} severity={severity} variant="filled" sx={{ width: '100%' }}>
        {msg}
      </Alert>
    </Snackbar>
  );
};

export default Notification;
