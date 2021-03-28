import React, { useEffect, useState } from 'react';
import { Champion } from '../api';
import useFetch from 'react-fetch-hook';
import { Button, Select } from 'grommet';
import { API_URL } from '../api/routes';
import { RouteComponentProps, navigate } from '@reach/router';

export const ChampionSearch: React.FC<RouteComponentProps> = () => {
  const { isLoading, data } = useFetch<Champion[]>(`${API_URL}/champions/`);
  const [searchOptions, setSearchOptions] = useState<string[]>([]);
  const [searchValue, setSearchValue] = useState('');

  useEffect(() => {
    if (data) {
      const championNames = data?.map((champion: Champion) => champion.name);
      setSearchOptions(championNames);
    }
    
  }, [!!isLoading]);

  const handleSearch = (search: string) => {
    if (data) {
      const filteredSearchOptions = data.filter(champion => champion.name.toLowerCase().includes(search.toLowerCase()));
      setSearchOptions(filteredSearchOptions.map((champion: Champion) => champion.name));
    }
  };

  if (!data) {
    return <div></div>
  } else {
    return (
      <section id="search">
        <p>
          Enter a champion in the search box to view statistics about their rotation history and get a prediction on when they will be free next.
        </p>
  
        <Select
          options={searchOptions}
          onChange={({ option }) => setSearchValue(option)}
          onSearch={handleSearch}
        />
        <Button primary label="View Champion" onClick={() => navigate(`/champions/${searchValue}`)} />
      </section>
    );
  }

  
};
