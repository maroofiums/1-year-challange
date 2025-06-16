import React from 'react';

const Button = ({ label, onClick }) => {
  return (
    <button onClick={onClick} style={{ margin: '10px', padding: '10px 20px' }}>
      {label}
    </button>
  );
};

export default Button;
