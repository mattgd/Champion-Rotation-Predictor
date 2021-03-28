import { Router } from '@reach/router';
import { Box, Grid, Grommet, Heading } from 'grommet';
import React, { useState } from 'react';
import { Champion } from './api';
import './App.css';
import { ChampionRotation, ChampionSearch } from './components';
import { ChampionView, HomeView } from './views';

const theme = {
  global: {
  },
  button: {
    border: {
      radius: '0px 5px 5px 0px',
    },
  },
  // select: {
  //   border: {
  //     radius: '5px 0px 5px 5px',
  //   },
  // }
};


function App() {
  const [currentRotationChampions, setCurrentRotationChampions] = useState<Champion[]>([]);
  const [nextRotationChampions, setNextRotationChampions] = useState<Champion[]>();

  return (
    <div className="App">
      <Grommet theme={theme}>
        <Grid
          rows={['xsmall', 'small']}
          columns={['medium']}
          gap="small"
          areas={[
            { name: 'header', start: [0, 0], end: [1, 0] },
            { name: 'nav', start: [0, 1], end: [0, 1] },
            { name: 'main', start: [1, 1], end: [1, 1] },
          ]}
        >
          <Box gridArea="header" background="brand">
            <header>
              <Heading>League of Legends Champion History</Heading>
              <Heading size="small">Free Champion Rotation Predictor</Heading>
            </header>
          </Box>
          <Box gridArea="nav" background="light-5">
            <ChampionSearch />
          </Box>
          <Box gridArea="main" background="light-2">
            <Router>
              <HomeView default path="/" />
              <ChampionView path="/champions/:name" />
            </Router>
          </Box>
        </Grid>
      </Grommet>
    </div>
  );
}

export default App;
