'use strict';

const sortYear = (movies) => movies.sort(yearComparator);

const sortTitle = (movies) => movies.sort(titleComparator);

const inGenre = (movies, genre) => movies.filter(movie => movie.genres.includes(genre));

const yearComparator = (a, b) => {
  if (a.year - b.year < 0) return -1;
  else if (a.year - b.year > 0) return 1;
  else return 0;
};

const titleComparator = (a, b) => {
  const titleA = a.title.replace(/^(A |The )/, '');
  const titleB = b.title.replace(/^(A |The )/, '');
  if (titleA < titleB) return -1;
  else if (titleA > titleB) return 1;
  else return 0;
};

module.exports = { sortYear, sortTitle, inGenre, yearComparator, titleComparator };
