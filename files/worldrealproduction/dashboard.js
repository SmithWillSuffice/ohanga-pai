const CUSTOM_POPUP_ENABLED=false;
const HOVER_READOUT_MS=30000;
const HOVER_DISMISS_ON_OUTSIDE_CLICK=true;
if(CUSTOM_POPUP_ENABLED){
document.querySelectorAll('.plot .js-plotly-plot').forEach(plot=>{
 const frame=plot.closest('.plot');
 const readout=document.createElement('div');
 readout.className='hover-readout';readout.hidden=true;readout.setAttribute('role','status');
 frame.appendChild(readout);
 let expiryTimer=null;
 plot.on('plotly_hover',event=>{
   if(!event.points||!event.points.length)return;
   readout.replaceChildren();
   const year=document.createElement('strong');
   year.textContent=String(event.points[0].x);
   readout.appendChild(year);
   const unit=plot.layout.yaxis?.title?.text||'';
   event.points.slice(0,12).forEach(point=>{
     if(!Number.isFinite(Number(point.y)))return;
     const line=document.createElement('span');line.className='hover-line';
     const name=point.data?.name||'World';
     line.textContent=name+': '+Number(point.y).toLocaleString(undefined,{maximumSignificantDigits:5})+(unit?' '+unit:'');
     readout.appendChild(line);
   });
   readout.hidden=false;
   if(expiryTimer!==null)clearTimeout(expiryTimer);
   expiryTimer=setTimeout(()=>{readout.hidden=true;expiryTimer=null},HOVER_READOUT_MS);
 });
 // Deliberately do not dismiss on plotly_unhover: the readout persists.
});
document.addEventListener('click',event=>{
 if(!HOVER_DISMISS_ON_OUTSIDE_CLICK)return;
 document.querySelectorAll('.hover-readout:not([hidden])').forEach(readout=>{
   if(!readout.contains(event.target))readout.hidden=true;
 });
});
}
function refreshPlots(pane){
 const selected=new Set(Array.from(pane.querySelectorAll('[data-country]:checked'),el=>el.dataset.country));
 pane.querySelector('.selected-count').textContent=selected.size+' selected';
 pane.querySelectorAll('.plot:not(.world-absolute) .js-plotly-plot').forEach(plot=>{
   const states=plot.data.map(trace=>trace.meta&&trace.meta.country?selected.has(trace.meta.country):true);
   const legend=plot.data.map((trace,i)=>Boolean(trace.meta&&trace.meta.country&&states[i]));
   Plotly.restyle(plot,{visible:states,showlegend:legend});
 });
}
document.querySelectorAll('.tab-pane').forEach(pane=>{
 const inputs=Array.from(pane.querySelectorAll('[data-country]'));
 const shortcuts=Array.from(pane.querySelectorAll('[data-rank]'));
 inputs.forEach(input=>input.addEventListener('change',()=>{
   shortcuts.forEach(box=>box.checked=false);
   refreshPlots(pane);
 }));
 shortcuts.forEach(box=>box.addEventListener('change',()=>{
   if(!box.checked){box.checked=true;return}
   shortcuts.forEach(other=>{if(other!==box)other.checked=false});
   const ranking=JSON.parse(pane.dataset.countryRanking);
   const allowed=new Set(ranking.slice(0,box.dataset.rank==='all'?ranking.length:Number(box.dataset.rank)));
   inputs.forEach(input=>{input.checked=allowed.has(input.dataset.country)});
   refreshPlots(pane);
 }));
 pane.querySelector('[data-world-absolute]').addEventListener('change',event=>{
   const section=pane.querySelector('.world-absolute');
   section.hidden=!event.target.checked;
   if(event.target.checked){Plotly.Plots.resize(section.querySelector('.js-plotly-plot'))}
 });
 pane.querySelector('.country-search').addEventListener('input',event=>{
   const needle=event.target.value.trim().toLowerCase();
   inputs.forEach(input=>{input.closest('.country-item').hidden=!input.closest('.country-item').textContent.toLowerCase().includes(needle)});
 });
 pane.querySelectorAll('[data-preset]').forEach(button=>button.addEventListener('click',()=>{
   shortcuts.forEach(box=>box.checked=false);
   inputs.forEach(input=>{input.checked=false});
   refreshPlots(pane);
 }));
});
document.querySelectorAll('[data-tab]').forEach(button=>button.addEventListener('click',()=>{
 document.querySelectorAll('.tab-btn').forEach(el=>{el.classList.remove('active');el.setAttribute('aria-selected','false')});
 document.querySelectorAll('.tab-pane').forEach(el=>el.classList.remove('active'));
 button.classList.add('active');button.setAttribute('aria-selected','true');
 const pane=document.getElementById('pane-'+button.dataset.tab);pane.classList.add('active');
 pane.querySelectorAll('.js-plotly-plot').forEach(el=>Plotly.Plots.resize(el));
}));