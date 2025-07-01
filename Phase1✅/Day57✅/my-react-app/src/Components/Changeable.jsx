import React, { useState } from 'react'


const Changeable = () => {
const [Count, setCount] = useState(0);
  return (
    <div>
        <h1>The value is {Count}</h1>
        <button onClick={()=>setCount(Count+1)}>Increase</button>
    </div>
  )
}

export default Changeable;