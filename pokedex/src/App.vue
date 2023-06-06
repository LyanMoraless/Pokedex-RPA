<template>
  <div>

    <div style="display: flex; justify-content: center; align-items: center;">
      <div class="margin-title">
        <text class="title">Pokedex</text>
    </div>
    <div class="row">a</div>
    </div>

    <div v-for="page in pages" :key="page.id" v-show="page.active">
      <table>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Poder</th>
          <th>Vida</th>
          <th>Ataque</th>
          <th>Forte Contra</th>
          <th>Fraco Contra</th>
        </tr>
        <tr v-for="pokemon in page.pokemons" :key="pokemon.name">
          <td>{{ pokemon.id }}</td>
          <td :class="pokemon.type">{{ pokemon.name }}</td>
          <td>{{ pokemon.power }}</td>
          <td>{{ pokemon.life }}</td>
          <td>{{ pokemon.attack }}</td>
          <td>{{ pokemon.strongAgainst }}</td>
          <td>{{ pokemon.weakAgainst }}</td>
        </tr>
      </table>
    </div>
    <div class="btns">
      <button class="btn" @click="showPage(1)">Page 1</button>
      <button class="btn" @click="showPage(2)">Page 2</button>
      <button class="btn" @click="showPage(3)">Page 3</button>
    </div>
    <div class="row-final">a</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pages: [
        {
          id: 1,
          active: true,
          pokemons: [],
        },
        {
          id: 2,
          active: false,
          pokemons: [],
        },
        {
          id: 3,
          active: false,
          pokemons: [],
        },
      ],
    };
  },
  mounted() {
    this.fetchPokemons();
  },
  methods: {
  async fetchPokemons() {
    try {
      const response = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=90');
      const pokemons = response.data.results;
      const pokemonDetails = await this.fetchPokemonDetails(pokemons);

      this.splitPokemonsIntoPages(pokemonDetails);
    } catch (error) {
      console.log(error);
    }
  },
  async fetchPokemonDetails(pokemons) {
    const pokemonDetails = [];
    for (const [index, pokemon] of pokemons.entries()) {
      try {
        const response = await axios.get(pokemon.url);
        const { name, stats, types } = response.data;
        const power = stats.find((stat) => stat.stat.name === 'special-attack').base_stat;
        const life = stats.find((stat) => stat.stat.name === 'hp').base_stat;
        const attack = stats.find((stat) => stat.stat.name === 'attack').base_stat;
        const strongAgainst = types.map((type) => type.type.name).join(', ');

        const weaknessesResponse = await axios.get(`https://pokeapi.co/api/v2/type/${types[0].type.name}`);
        const weaknesses = weaknessesResponse.data.damage_relations.double_damage_from.map(type => type.name).join(', ');

        pokemonDetails.push({
          id: index + 1,
          name,
          power,
          life,
          attack,
          strongAgainst,
          weakAgainst: weaknesses,
          type: types[0].type.name,
        });
      } catch (error) {
        console.log(error);
      }
    }
    return pokemonDetails;
  },
  splitPokemonsIntoPages(pokemonDetails) {
    let currentPage = 1;
    let currentIndex = 0;

    this.pages = [];

    while (currentIndex < pokemonDetails.length) {
      const pagePokemons = pokemonDetails.slice(currentIndex, currentIndex + 30);
      this.pages.push({
        id: currentPage,
        active: currentPage === 1,
        pokemons: pagePokemons,
      });

      currentIndex += 30;
      currentPage++;
    }
  },
  showPage(page) {
    this.pages.forEach((pageObj) => {
      pageObj.active = pageObj.id === page;
    });
  },
},
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 100px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.page {
  display: none;
}

.page.active {
  display: block;
}
.btns{
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
  margin-left: 42%;
  margin-right: 42%;
}
.btn{
  padding: 15px;
  border-radius: 200px;
  border-color: red;
  background-color: transparent;
  color: red;
}
.margin-title{
  padding-bottom: 20px;
}
.title{
  font-size: 60px;
  font-family: 'pokemon';
}
.row{
  background-color: red;
  border-width: 100px;
  width: 100%;
  height: 20px;
  color: transparent;
  margin-left: 40px;
  border-end-end-radius: 10px;
  border-start-end-radius: 10px;
}
.row-final{
  background-color: red;
  border-width: 100px;
  width: 100%;
  height: 20px;
  color: transparent;
  border-radius: 10px;
  margin-top: 30px;
}
</style>