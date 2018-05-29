import axios from 'axios';

// TODO (Andrey)
// API_ROOT for development env
const API_ROOT = 'api';

const responseBody = res => res.data;

const requests = {
  get: url =>
    axios
    .get(`${API_ROOT + url}/`).then(responseBody),
};

const Events = {

  // Should be removed if possible
  // it`s better to use the backend checker instead
  load: () =>
    requests.get('/events', {}),
};

export default {
    Events,
};
