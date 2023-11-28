<template>
  <div class="head">
    <div class="title">
      AlphaNum Predictor
    </div>
    <div class="body">
    <div class="input-box">
      <div class="text-img-wrap">
        Upload image containing classes 0-9 or A-Z
        <input class="file-input" type="file" @change="handleImageUpload" accept="image/*" />
      </div>

    </div>
    <div class="uploaded-img" v-if="imageUrl">
      <div class="text-img-wrap">
        Uploaded image:
        <img :src="imageUrl" style="width:50px">
      </div>

    </div>
    <div class="label" v-if="label">
      <div class="text-img-wrap">
        Predicted label:
        <div class="label-text">
          <b>{{ label }}</b>
        </div>
      </div>

    </div>
    </div>
    <footer class="footer">
      <div class="social-media">
        <a href="https://instagram.com/go_cool_ram"><img src="./assets/instagram.png" style="width:50px;"></a>
        <a href="https://www.linkedin.com/in/gokul-ram-s-0277b0108/"><img src="./assets/linkedin.png" style="width:50px;"></a>
      </div>
      <div class="footer-text">
        Created by Gokul Ram Subramani
      </div>
    </footer>
  </div>

</template>


<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export default Vue.extend( {
  name: 'App',
  data(){
    return{
    imageUrl:null,
    label:null,
  }
},
  methods:{
    async handleImageUpload(event){
      const file = event.target.files[0];
      this.imageUrl = URL.createObjectURL(file);
      const formData = new FormData();
      formData.append('image', file);

      const response = await axios.post('http://127.0.0.1:5000/predict', formData);
      this.label=response.data.label
    }
  }
})
</script>

<style>
html,body {
    margin: 0 !important;
}
.head{
  font-family:bradley hand,cursive;
  font-size:20px;
  width:100%;
}
.title{
  font-family: bradley hand,cursive;
  font-size:30px;
  text-align: center;
  color: rgb(249, 231, 231);
  background: rgb(6, 6, 59);
  padding:5%;
  margin-bottom: 100px;
}
.body{
  display: flex;
  width:90%;
  gap:5%;
  margin:auto;
  justify-content: center;
  @media(max-width:700px){
    flex-direction: column;
    width:100%;
  }
}
.input-box{
  border: 1px solid grey;
  padding:5%;
  border-style:dashed;
  background: rgb(207, 207, 255);
  border-radius:10px;
  cursor: pointer;
  width:30%;
  position: relative;
  @media(max-width:700px){
    width:90%;
  }

}
.input-box:hover{
  background:rgb(158, 158, 244);
}
.file-input{
  width:100%;
  height:100%;
  position:absolute;
  cursor:pointer;
  opacity:0;

}
.uploaded-img{
  border: 1px solid grey;
  border-radius: 10px;
  border-style:dashed;
  padding:2%;
  padding-top:0;
  width:30%;
  @media(max-width:700px){
    width:90%;
  }

}
.label{
  padding:2%;
  padding-top:0;
  border: 1px solid grey;
  border-radius: 10px;
  border-style:dashed;
  width:30%;
  @media(max-width:700px){
    width:90%;
  }

}

.text-img-wrap{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap:50px;
}

.footer{
  background:rgb(6, 6, 59);
  width:100%;
  color: rgb(249, 231, 231);
  position: absolute;
  bottom:0;
  display:flex;
  flex-direction: column;
  align-items: center;


}
.label-text{
  font-family: 'Unbounded';
  font-size:30px;
}
.social-media{
  display: flex;
  gap:20%;
  margin:10px;
}
</style>
