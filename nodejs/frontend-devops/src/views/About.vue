<template>
  <div class="body">
    <vs-row vs-justify="space-between">
      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
       <vs-button class="tile-unit" color="primary" type="border">
          <h6>Unité de production</h6>
          <vs-row>
            <i class="material-icons">memory</i> 
            <h2>1</h2>
          </vs-row>
        </vs-button>
      </vs-col>
      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
          <vs-button class="tile-unit" color="primary" type="border">
            <h6>Unité de production</h6>
            <vs-row>
              <i class="material-icons">memory</i> 
              <h2>2</h2>
            </vs-row>
          </vs-button>
      </vs-col>
      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <vs-button class="tile-unit" color="primary" type="border">
            <h6>Unité de production</h6>
            <vs-row>
              <i class="material-icons">memory</i> 
              <h2>3</h2>
            </vs-row>
          </vs-button>
      </vs-col>
      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <vs-button class="tile-unit" color="primary" type="border">
            <h6>Unité de production</h6>
            <vs-row>
              <i class="material-icons">memory</i> 
              <h2>4</h2>
            </vs-row>
          </vs-button>
      </vs-col>
      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <vs-button class="tile-unit" color="primary" type="border">
            <h6>Unité de production</h6>
            <vs-row>
              <i class="material-icons">memory</i> 
              <h2>5</h2>
            </vs-row>
          </vs-button>
      </vs-col>
    </vs-row>
    <h1>Analyse automates</h1>
    <vs-tabs position="left" alignment="left">
      <vs-tab label="Température cuve">
        <div class="con-tab-ejemplo">
          <chartBrush></chartBrush>
        </div>
      </vs-tab>
      <vs-tab label="Température extérieure">
        <div class="con-tab-ejemplo">
        </div>
      </vs-tab>
      <vs-tab label="Poids lait en cuve">
        <div class="con-tab-ejemplo">login</div>
      </vs-tab>
      <vs-tab label="Poids produit réalisé">
        <div class="con-tab-ejemplo">Disabled</div>
      </vs-tab>
      <vs-tab label="Mesure pH">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
      <vs-tab label="Mesure K+">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
      <vs-tab label="Concentration de NaCl">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
      <vs-tab label="Niveau bactérien salmonelle">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
      <vs-tab label="Niveau bactérien E-coli">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
      <vs-tab label="Niveau bactérien Listéria">
        <div class="con-tab-ejemplo">Lorem ipsum dolor sit amet</div>
      </vs-tab>
    </vs-tabs>
    
  </div>
</template>

<script>
  import ChartBrush from "../components/ChartBrush.component";

  export default {
    components: {
      ChartBrush,
    },
    data: function() {
      return {
      }
    }
  };
</script>

<style>
.tile-unit {
  width: -webkit-fill-available;
  display: flex;
  justify-content: start;
  padding: 12px;
}
.tile-unit h6 {
  font-size: 11px;
  padding-bottom: 4px;
}
.tile-unit i {
  font-size: 24px;
  padding-top: 2px;
}
.tile-unit h2 {
  font-size: 28px;
  padding-left: 4px;
  font-weight: 700;
}
.body {
  padding: 48px;
}
h1 {
  width: max-content;
  font-size: 28px;
  font-weight: 900;
  color: #3a3a3a;
  padding-top: 40px;
  padding-bottom: 30px;
}
.con-ul-tabs {
  width: 270px !important;
}
.con-slot-tabs {
  width: 100%;
}
.vs-tabs-primary .line-vs-tabs {
    background: #1e74ff !important;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
}
.vs-tabs-position-left .vs-tabs--ul {
    border-right: 1px solid rgb(224, 224, 224) !important;
}
.vs-tabs--ul {
    -webkit-box-shadow: none !important;
    box-shadow:none !important;
}
.vs-tabs--btn {
  text-align: left;
}
</style>
