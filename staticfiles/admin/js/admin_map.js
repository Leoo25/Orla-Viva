document.addEventListener('DOMContentLoaded', function() {
    
    const latInput = document.getElementById('id_latitude');
    const lonInput = document.getElementById('id_longitude');
    
    if (!latInput || !lonInput) {
        return; 
    }
    
    const cepContainer = document.createElement('div');
    cepContainer.style.marginBottom = '10px';
    cepContainer.innerHTML = `
        <label for="cep_input" style="font-weight: bold; margin-right: 5px;">Buscar por CEP:</label>
        <input type="text" id="cep_input" placeholder="00000-000" style="width: 100px;">
        <button type="button" id="cep_search_btn" class="button">Buscar</button>
        <span id="cep_status" style="margin-left: 10px; font-size: 0.9em; color: #666;"></span>
    `;
    
    const mapDiv = document.createElement('div');
    mapDiv.id = 'admin-map-widget';
    mapDiv.style.height = '400px';
    mapDiv.style.marginBottom = '15px';
    
    const jazzminFormGroup = latInput.closest('.form-group');
    const standardFieldset = latInput.closest('fieldset');

    if (jazzminFormGroup) {
        jazzminFormGroup.parentNode.insertBefore(mapDiv, jazzminFormGroup);
        jazzminFormGroup.parentNode.insertBefore(cepContainer, mapDiv);
    } else if (standardFieldset) {
        standardFieldset.prepend(mapDiv);
        standardFieldset.prepend(cepContainer);
    } else {
        return;
    }

    const praiaGrandeLat = -24.0058;
    const praiaGrandeLon = -46.4028;

    let startLat = parseFloat(latInput.value) || praiaGrandeLat;
    let startLon = parseFloat(lonInput.value) || praiaGrandeLon;
    let startZoom = latInput.value ? 18 : 13; 
    
    const map = L.map(mapDiv).setView([startLat, startLon], startZoom);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const marker = L.marker([startLat, startLon], {
        draggable: true 
    }).addTo(map);

    function updateInputs(latlng) {
        latInput.value = latlng.lat.toFixed(6);
        lonInput.value = latlng.lng.toFixed(6);
    }

    marker.on('dragend', function(e) {
        updateInputs(e.target.getLatLng());
    });

    map.on('click', function(e) {
        marker.setLatLng(e.latlng); 
        updateInputs(e.latlng);     
    });
    
    if (latInput.value && lonInput.value) {
        updateInputs(marker.getLatLng());
    }
    
    const tabLink = document.querySelector('a[href="#fieldset-1"]'); 
    if (tabLink) {
        tabLink.addEventListener('shown.bs.tab', function() {
            map.invalidateSize();
        });
    }

    setTimeout(function() {
        map.invalidateSize();
    }, 50);

    document.getElementById('cep_search_btn').addEventListener('click', searchByCep);

    async function searchByCep() {
        const cepInput = document.getElementById('cep_input');
        const statusEl = document.getElementById('cep_status');
        const cep = cepInput.value.replace(/\D/g, ''); 

        if (cep.length !== 8) {
            statusEl.textContent = 'CEP inválido (8 dígitos).';
            statusEl.style.color = 'red';
            return;
        }

        statusEl.textContent = 'Buscando endereço (ViaCEP)...';
        statusEl.style.color = '#333';

        try {
            const viaCepResponse = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
            if (!viaCepResponse.ok) throw new Error('Falha na rede ao consultar ViaCEP.');
            const viaCepData = await viaCepResponse.json();

            if (viaCepData.erro) {
                statusEl.textContent = 'CEP não encontrado (ViaCEP).';
                statusEl.style.color = 'red';
                return;
            }
            
            let addressParts = [];
            if (viaCepData.logradouro) addressParts.push(viaCepData.logradouro);
            if (viaCepData.bairro) addressParts.push(viaCepData.bairro);
            if (viaCepData.localidade) addressParts.push(viaCepData.localidade);
            if (viaCepData.uf) addressParts.push(viaCepData.uf);
            addressParts.push('Brazil'); 
            const addressQuery = addressParts.join(', ');

            statusEl.textContent = `Buscando coordenadas para: ${addressQuery}...`;
            
            const nominatimResponse = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(addressQuery)}&format=json&addressdetails=0&limit=1`);
            if (!nominatimResponse.ok) throw new Error('Falha na rede ao consultar Nominatim.');
            
            const nominatimData = await nominatimResponse.json();
            
            if (nominatimData && nominatimData.length > 0 && nominatimData[0].lat && nominatimData[0].lon) {
                const result = nominatimData[0];
                const lat = parseFloat(result.lat);
                const lon = parseFloat(result.lon);
                
                map.setView([lat, lon], 17);
                marker.setLatLng([lat, lon]);
                updateInputs({ lat: lat, lng: lon });

                statusEl.textContent = `Encontrado: ${addressQuery.split(',')[0]}`;
                statusEl.style.color = 'green';
            
            } else {
                statusEl.textContent = 'Endereço encontrado, mas sem coordenadas.';
                statusEl.style.color = 'orange';
            }

        } catch (error) {
            console.error('Erro na busca por CEP:', error);
            statusEl.textContent = 'Erro. Verifique o console (F12).';
            statusEl.style.color = 'red';
        }
    }
});