import { RouteComponentProps } from '@reach/router';
import { Box, Heading, Image, Spinner, Text } from 'grommet';
import React  from 'react';
import useFetch from 'react-fetch-hook';
import { Champion } from '../api';
import { API_URL } from '../api/routes';

type MatchParams = {
  name: string
};

export const ChampionView: React.FC<RouteComponentProps<MatchParams>> = ({ name }) => {
  const { isLoading, data } = useFetch<Champion>(`${API_URL}/champions/${name}`);

  if (isLoading) {
    return <Spinner />;
  } else {
    return (
      <div className="champion">
        <Heading>{data?.name}</Heading>
        <Box height="medium" width="medium">
          <Image fit="cover" src={data?.image} a11yTitle={data?.name} />
        </Box>
        <Text>Blue Essence: {data?.blueEssence}</Text>
        <Text>Riot Points: {data?.riotPoints}</Text>
      </div>
    );
  }
};
