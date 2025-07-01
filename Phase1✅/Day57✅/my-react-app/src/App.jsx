import React from 'react';
import Useable from './Components/Useable';
import Editable from './Components/Editable';
import Changeable from './Components/Changeable';

const App = () => {
  return (
    <div>
      <h1>This is For Useable.jsx</h1>
      <Useable />

      <h1>This is for Editable.jsx</h1>
      <Editable name="Maroof" />

      <h1>This is For Changeable.jsx</h1>
      <Changeable />
    </div>
  );
}

export default App;
