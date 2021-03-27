import React, { useState } from 'react';
import { Champion } from '../api';
import useFetch from 'react-fetch-hook';
import { Select } from 'grommet';

export const ChampionSearch = () => {
  const { isLoading, data } = useFetch<Champion[]>("https://swapi.co/api/people/1");
  const [searchOptions, setSearchOptions] = useState<Champion[]>(data || []);
  const [searchValue, setSearchValue] = useState('');

  const submitSearch = (e: React.FormEvent<HTMLFormElement>) => {
    // Do the search
  };

  const handleSearch = (search: string) => {
    if (data) {
      const filteredSearchOptions = data.filter(champion => champion.name.includes(search));
      setSearchOptions(filteredSearchOptions);
    }
  };

  return (
    <section id="search">
      <p>
        Enter a champion in the search box to view statistics about their rotation history and get a prediction on when they will be free next.
      </p>

      <Select
        options={searchOptions}
        value={searchValue}
        onChange={({ option }) => setSearchValue(option)}
        onSearch={handleSearch}
      />
    </section>
  );
};
