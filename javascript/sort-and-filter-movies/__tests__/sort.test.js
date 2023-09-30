'use strict';

const moviesData = require('../movies');
const { sortYear, sortTitle, inGenre, yearComparator, titleComparator }  = require('../sort');

describe('Tests for sorter functions', () => {
  it('can sort movies by year', () => {
    const movies = sortYear(moviesData);
    expect(movies.map((m) => m.title)).toEqual([
      'The Cotton Club',
      'Crocodile Dundee',
      'Beetlejuice',
      'The Shawshank Redemption',
      'Memento',
      'City of God',
      'Ratatouille',
      'Stardust',
      'Valkyrie',
      'The Intouchables',
    ]);
  });

  it('can sort movies by title', () => {
    const movies = sortTitle(moviesData);
    expect(movies.map((m) => m.title)).toEqual([
      'Beetlejuice',
      'City of God',
      'The Cotton Club',
      'Crocodile Dundee',
      'The Intouchables',
      'Memento',
      'Ratatouille',
      'The Shawshank Redemption',
      'Stardust',
      'Valkyrie',
    ]);
  });

  it('can find movies by genre', () => {
    const movies = sortYear(inGenre(moviesData, 'Adventure'));
    expect(movies.map((m) => m.title)).toEqual([
      'Crocodile Dundee',
      'Stardust',
    ]);
  });
});

describe('Tests for comparator functions', () => {
  const movieA =   {
    title: 'The Cotton Club',
    year: 1984,
    genres: ['Crime', 'Drama', 'Music'],
  };
  const movieB =   {
    title: 'Memento',
    year: 2000,
    genres: ['Mystery', 'Thriller'],
  };

  it('correctly returns -1 when a.year is less than b.year', () => {
    expect(yearComparator(movieA, movieB)).toEqual(-1);
  });

  it('correctly returns 1 when a.year is greater than b.year', () => {
    expect(yearComparator(movieB, movieA)).toEqual(1);
  });

  it('correctly returns 0 when a.year is the same as b.year', () => {
    expect(yearComparator(movieB, movieB)).toEqual(0);
  });

  it('correctly returns -1 when a.title is less than b.title', () => {
    expect(titleComparator(movieA, movieB)).toEqual(-1);
  });

  it('correctly returns 1 when a.title is greater than b.title', () => {
    expect(titleComparator(movieB, movieA)).toEqual(1);
  });

  it('correctly returns 0 when a.title is the same as b.title', () => {
    expect(titleComparator(movieB, movieB)).toEqual(0);
  });
});
