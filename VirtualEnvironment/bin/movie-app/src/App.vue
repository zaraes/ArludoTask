<template>
  <input v-model="searchRequest" placeholder="search movies" v-on:keyup.enter="searchMovies">
    <button @click='buttonClick()'>
        search
    </button>
    <p v-text= "searchRequest"></p>


  
  <ul class="list-group">
    <li class="list-group-item" v-for='movie in movies' :key='movie.id'>
      <div id="movie">
      <h4>{{movie.title}} - {{movie.rating}}</h4>
      {{movie.poster}}
      <img src="{{movie.poster}}" alt="Poster">
    </div>
    
    <br>
    </li>
  </ul>
  
  
</template>

<script>
// fetch('/api/movies').then(res => {
//   this.movies = res['movies']
// }) instead of vvvvvvvvvv

//  https://v3.vuejs.org/api/options-lifecycle-hooks.html
//  https://cli.vuejs.org/guide/deployment.html#github-pages <- building it as a static site to serve on backend ... if you get to it ... no pressure if not.

import movie_metadata from '/Users/zara/Arludo/VirtualEnvironment/bin/movie-app/data/movie_metadata.json'
import theatre_showtimes from '/Users/zara/Arludo/VirtualEnvironment/bin/movie-app/data/theater_showtimes.json'

export default {
  name: 'App',
  components: {},
  data() {
    return {
      movies: []
    }
  },
  mounted() {
    // runs on initialization of the component
    console.log(movie_metadata)
    // movie_metadata.forEach(movie => {
    //   newMovie = {
    //     ...movie,
    //     showTimes: {
    //       "pacificTheatre": []
    //     }
    //   }
    // })
    this.movies = movie_metadata
    console.log(theatre_showtimes)

  //   theatre_showtimes.forEach(theatre => {
  //     theatre.showTimes.keys().forEach(movieKey => {
  //       let showTimes = theatre.showTimes[movieKey]
  //     })
  //   })
  },
  methods: {
    buttonClick() {
      console.log('yaya')
    }
  }
}
</script>

<style>
  .list-group {
    list-style-type: none;
    margin: 0;
    padding: 0;
    text-align: center;
  }
  #movie {
    
    background-color: lightblue;
    text-align: center;
    max-width: 500px;
    width: 50%;
    margin: auto;
    padding: 10px;
  }
  
</style>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

