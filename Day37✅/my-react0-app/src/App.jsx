import React from 'react'
import Greeting from './components/greeting'
import User from './components/User'
import Counter from './components/Counter'

const App = () => {
  return (
    <div>
      <Greeting />
      <User name="Maroof"/>
      <User name="Tanvir"/>
      <Counter/>
    </div>
  )
}

export default App