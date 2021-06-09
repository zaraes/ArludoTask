<template>
  <input id = "search-bar" v-model="search" placeholder="search movies" size=50>
    
    <br><br>

          
      <span v-for='theater in theaters' :key='theater.name'>
        <button v-on:click="currTheaterName; setTheatre(theater.name)">{{theater.name}}</button>
        
      </span>
    
    <br><br>
  <ul class="list-group">
    <li class="list-group-item" v-for='movie in filteredMovies' :key='movie.id'>
      <div id="movie" height=auto width=auto style="overflow:auto">
        <img v-bind:src = "movie.poster" alt = "Poster" width = 200 align="left">
        <h4>{{movie.title}}</h4> <h5>{{movie.rating}}</h5>
        <span id = "times">
        <li v-for='time in movie.showTimes[currTheaterName]' :key='time'>
          <div id = "time">{{time}}</div>
        </li>
        </span>

        
        <br><br>
        
      </div>
      <br>
    </li>
  </ul>
  

</template>

<script>

import movie_metadata from './data/movie_metadata.json'
import theatre_showtimes from './data/theater_showtimes.json'

export default {
  name: 'App',
  components: {},
  data() {
    return {
      movies: [],
      search: '',
      currTheaterName: theatre_showtimes[0].name
    }
    
  },
  mounted() {
    this.movies = movie_metadata
    this.theaters = theatre_showtimes

    
    this.movies.forEach(currMovie => {
      currMovie["showTimes"] = {}
    })
    console.log(theatre_showtimes)
    this.searchRequest = ''
    theatre_showtimes.forEach(theatre => {
      Object.keys(theatre.showtimes).forEach(movieKey => {
        let showTimes = theatre.showtimes[movieKey]
        this.movies.forEach(movObj=>{
          if(movObj.id == movieKey) {movObj["showTimes"][theatre.name] = showTimes}
        })
      })
    })
  },

  watch: {
    search() {
      this.backdoor++;
    },
  },
  // URL: 
  computed: {
    filteredMovies: function() {     
      return (this.movies.filter((movie) => {
        return movie.title.toLowerCase().match(this.search.toLowerCase()) && this.currTheaterName in movie.showTimes;
      }));
    }
  },

  methods:{
    setTheatre: function(theatreName){
      this.currTheaterName = theatreName
      console.log("Changing Theatre: "+this.currTheatre)
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
    background-color: white;
    text-align: center;
    max-width: 500px;
    width: 50%;
    margin: auto;
    padding: 10px;
    -moz-box-shadow:   0 0 10px #A9ABAB;
   -webkit-box-shadow: 0 0 10px #A9ABAB;
   box-shadow:         0 0 10px #A9ABAB;
   border-radius: 25px;
  }
  h4 {

  }
  h5 {

    color: #878787;
  }

  img{
    text-align: left;
    padding-left: 5px;
    padding-top: 5px;
    padding-bottom: 5px;
    
  }
  body {
    background-color: #DADFE3
  }

  #search-bar {
    border-radius: 10px;
    border-color: #DADFE3;
  }

  button {
    background-color: #DADFE3;
    border-radius: 25px;
    border-style: none;
  }

  #times{
    display:inline-block;

  }

  #time {
    display:inline;
    text-align: center;
  }

  p {
    font-size: 5px;
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

