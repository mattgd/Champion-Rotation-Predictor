import React from 'react';
import { Link } from '@reach/router';
import { Champion } from '../api';

export const ChampionRotation: React.FC<{ champions: Champion[] }> = ({ champions }) => (
  <article className="rotation">
    <ul>
      {champions.map((champion: Champion) => (
        <li>
          <Link to={`/champion/${champion.name}`}>
            <img src={champion.image} alt={champion.name} />
            <span className="champion_name">{champion.name}</span>
          </Link>
        </li>
      ))}
    </ul>
  </article>
);
