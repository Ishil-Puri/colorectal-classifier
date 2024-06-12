import React from 'react';
import './App.css';

import { HomePage } from './components/HomePage';
import { FluentProvider, webLightTheme } from '@fluentui/react-components';


function App() {
  return (
  <FluentProvider theme={webLightTheme}>
    <HomePage></HomePage>
  </FluentProvider>
  );
}

export default App;
