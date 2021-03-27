import { Box, Grid, Heading } from 'grommet';
import React, { useState } from 'react';
import { Champion } from './api';
import './App.css';
import { ChampionRotation, ChampionSearch } from './components';

function App() {
  const [currentRotationChampions, setCurrentRotationChampions] = useState<Champion[]>([]);
  const [nextRotationChampions, setNextRotationChampions] = useState<Champion[]>();
  
  return (
    <div className="App">
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
        <Box gridArea="nav" background="light-5" />
        <Box gridArea="main" background="light-2">
          <ChampionSearch />

          <h1>Current Rotation</h1>
          <ChampionRotation champions={currentRotationChampions} />

          {nextRotationChampions &&
            <>
              <h1>Next Week's Rotation</h1>
              <ChampionRotation champions={nextRotationChampions} />
            </>
          }
        </Box>
      </Grid>
    </div>
  );
}

export default App;
