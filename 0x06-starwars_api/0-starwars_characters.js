#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const allCharacters = JSON.parse(body).characters;
    const charactersName = allCharacters.map(
      (url) => new Promise((resolve, reject) => {
        request(url, (reqError, __, respose) => {
          if (reqError) {
            reject(reqError);
          }
          resolve(JSON.parse(respose).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
