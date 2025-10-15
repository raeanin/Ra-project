<template>
  <div class="bg-white min-h-screen text-white flex items-center justify-center">
    <div class="flex flex-col items-center text-center">
      
      
      <img 
        src="/IMG_1396.gif" 
        alt="Animation 1" 
        class="w-94 h-64 mb-6 rounded-xl shadow-lg object-cover"
      />

      <h1 class="text-2xl font-extrabold mb-4 animate-pulse">
      Login Ra factory
    </h1>

      
      <button
  @click="login"
  class="mt-6 w-64 px-6 py-3 bg-purple-600 text-white font-semibold rounded-lg hover:bg-purple-800 shadow-lg transition duration-300"
>
  Login
</button>

    </div>
  </div>
</template>

<script setup>
const login = () => {
  localStorage.setItem("loggedIn", "true");
  alert(" You are logged in!");
  window.location.href = "/"; 
};
</script>
