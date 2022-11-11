<template>
  <Navbar/>
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow p-3 mb-5 bg-body rounded text-dark" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <div class="mb-md-5 mt-md-4 pb-5">
              <form>
                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                <p class="text-white-50 mb-5">Please enter your email and password!</p>
                <!-- Email input -->
                <div class="form-outline form-white mb-4">
                  <input id="typeEmailX" class="form-control form-control-lg" type="email" placeholder="Email"/>

                </div>

                <div class="form-outline form-white mb-4">
                  <input id="typePasswordX" class="form-control form-control-lg" type="password" placeholder="Password"/>
                </div>

                <!-- Submit button -->
                <button class="btn btn-primary btn-lg px-5" type="submit" @click="$router.push({name: 'home'})">Login</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import Navbar from "@/components/Navbar.vue"

export default {
  components: {
    Navbar,
  }

};
</script>

<style lang="scss" scoped>


</style>
