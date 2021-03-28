import { RouteComponentProps } from '@reach/router';
import React, { useState } from 'react';
import { Champion } from '../api';

import { ChampionRotation } from '../components';

export const HomeView: React.FC<RouteComponentProps> = () => {
  const [currentRotationChampions, setCurrentRotationChampions] = useState<Champion[]>([]);
  const [nextRotationChampions, setNextRotationChampions] = useState<Champion[]>();

  return (
    <>
      <h1>Current Rotation</h1>
      <ChampionRotation champions={currentRotationChampions} />

      {nextRotationChampions &&
        <>
          <h1>Next Week's Rotation</h1>
          <ChampionRotation champions={nextRotationChampions} />
        </>
      }
    </>
  );
}
