# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from main.forms.userforms import LoginForm
from main.forms.liquidacionForms import liquidacionForm

def simularLiquidacion_view(request):
    
    datos_liquidacion = {
            'ingreso_minimo_men': '460000', #dejar fijo, deseable base de datos.
            'valor_utm': '64666',    #obtener desde api
            'valor_uf': '36733.04',  #obtener desde api
            'tope_imponible_uf_afpsalud': '84.3', #dejar fijo
            'tope_imponible_seg_ces': '126.6',    #dejar fijo
            'contrato_indef': 'SI',
            'aporte_seg_ces': '0.006',
            'sueldo_base': '0', #Como ejemplo se asigna un millon
            'dias_trabajados': '30',
            'dias_no_trabajados': '0',
            'otros_ingresos': '0' , #Corresponde a bonos, aguinaldos, seguro vida colectivo
            'asignaciones': '0', #corresponde asignacion teletrabajo, transporte y colacion
            'descuentos': '0', #corresponde asignacion teletrabajo, transporte y colacion
            'costo_plan_isapre' : 0, 
            'tasa' : 0, 
            'rebaja' : 0
            
        }
    #Este primer if es para cuando el usuario envia datos
    if request.method == 'POST':
        form = liquidacionForm(data=request.POST)
        
        if form.is_valid():
            #Aca debo utilizar los datos qaue ingrso el usuario

            sueldo_base_usuario = form.cleaned_data['sueldo_base']
            otros_ingresos = form.cleaned_data['otros_ingresos']
            asignaciones = form.cleaned_data['asignaciones']
            descuentos = form.cleaned_data['descuentos']
            costo_plan_isapre = form.cleaned_data['costo_plan_isapre']
            
            datos_liquidacion['sueldo_base'] = sueldo_base_usuario  # Actualiza valor_uf con el sueldo base del usuario
            datos_liquidacion['otros_ingresos'] = otros_ingresos
            datos_liquidacion['asignaciones'] = asignaciones
            datos_liquidacion['descuentos'] = descuentos
            datos_liquidacion['costo_plan_isapre'] = costo_plan_isapre

    else:
        #Genero el form vacio en caso de ser GET 
        form = liquidacionForm()


    valor_uf = float(datos_liquidacion['valor_uf'])
    tope_imponible_clp_afpsalud = valor_uf * float(datos_liquidacion['tope_imponible_uf_afpsalud'])
    
    ingreso_minimo = float(datos_liquidacion['ingreso_minimo_men'])
    sueldo_base = float(datos_liquidacion['sueldo_base'])
    ingresos1 = float(datos_liquidacion['otros_ingresos'])
    gratificacion = (ingreso_minimo * 4.75 / 12) if (ingreso_minimo * 4.75 / 12) < (sueldo_base / 4) else (sueldo_base / 4)
    total_hab_imp = sueldo_base + gratificacion + ingresos1
    total_hab_no_imp = float(datos_liquidacion['asignaciones'])

    cotizacion_obl_afp = min(total_hab_imp, tope_imponible_clp_afpsalud) * (0.10 + 0.0127)
    pago_electronico_obl_afp = min(total_hab_imp, tope_imponible_clp_afpsalud) * (0.10)
    cotizacion_salud  = min(total_hab_imp, tope_imponible_clp_afpsalud) * (0.07)


    tiuf = float(datos_liquidacion['tope_imponible_seg_ces'])
    segur_cesantia = min(total_hab_imp, tiuf * valor_uf) * 0.006 if datos_liquidacion['contrato_indef'] == "SI" else 0
    
    costo_plan_isapre = float(datos_liquidacion['costo_plan_isapre'])
    adicional_salud = costo_plan_isapre * valor_uf - cotizacion_salud if costo_plan_isapre * valor_uf > cotizacion_salud else 0
    
    sueldo_antes_impuesto = total_hab_imp - cotizacion_obl_afp -adicional_salud - cotizacion_salud - segur_cesantia
    tasa_imp_unico_cat = 1
    rebaja = 1
    impuesto_unico_cat = 1
    sueldo_liquido = 1
    datos_liquidacion['tope_imponible_clp_afpsalud'] = tope_imponible_clp_afpsalud
    datos_liquidacion['gratificacion'] = gratificacion
    datos_liquidacion['total_hab_imp'] = total_hab_imp
    datos_liquidacion['total_hab_no_imp'] = total_hab_no_imp
    datos_liquidacion['cotizacion_obl_afp'] = cotizacion_obl_afp
    datos_liquidacion['cotizacion_salud'] = cotizacion_salud
    datos_liquidacion['pago_electronico_obl_afp'] = pago_electronico_obl_afp
    datos_liquidacion['segur_cesantia'] = segur_cesantia
    datos_liquidacion['sueldo_antes_impuesto'] = sueldo_antes_impuesto
    datos_liquidacion['tasa_imp_unico_cat'] = tasa_imp_unico_cat
    datos_liquidacion['adicional_salud'] = adicional_salud

    tramos_impuesto = [
    {"Periodo": "MENSUAL", "Desde": "0", "Hasta": "$ 879.957,00", "Factor": 0, "Cantidad a Rebajar": "0", "Tasa de Impuesto Efectiva": "Exento"},
    {"Periodo": "MENSUAL", "Desde": "$ 879.957,01", "Hasta": "$ 1.955.460,00", "Factor": 0.04, "Cantidad a Rebajar": "$ 35.198,28", "Tasa de Impuesto Efectiva": "2,20%"},
    {"Periodo": "MENSUAL", "Desde": "$ 1.955.460,01", "Hasta": "$ 3.259.100,00", "Factor": 0.08, "Cantidad a Rebajar": "$ 113.416,68", "Tasa de Impuesto Efectiva": "4,52%"},
    {"Periodo": "MENSUAL", "Desde": "$ 3.259.100,01", "Hasta": "$ 4.562.740,00", "Factor": 0.135, "Cantidad a Rebajar": "$ 292.667,18", "Tasa de Impuesto Efectiva": "7,09%"},
    {"Periodo": "MENSUAL", "Desde": "$ 4.562.740,01", "Hasta": "$ 5.866.380,00", "Factor": 0.23, "Cantidad a Rebajar": "$ 726.127,48", "Tasa de Impuesto Efectiva": "10,62%"},
    {"Periodo": "MENSUAL", "Desde": "$ 5.866.380,01", "Hasta": "$ 7.821.840,00", "Factor": 0.304, "Cantidad a Rebajar": "$ 1.160.239,60", "Tasa de Impuesto Efectiva": "15,57%"},
    {"Periodo": "MENSUAL", "Desde": "$ 7.821.840,01", "Hasta": "$ 20.206.420,00", "Factor": 0.35, "Cantidad a Rebajar": "$ 1.520.044,24", "Tasa de Impuesto Efectiva": "27,48%"},
    {"Periodo": "MENSUAL", "Desde": "$ 20.206.420,01", "Hasta": "Y MÁS", "Factor": 0.4, "Cantidad a Rebajar": "$ 2.530.365,24", "Tasa de Impuesto Efectiva": "MÁS DE 27,48%"}
    ]
    tasa = 0
    rebaja = 0
    for tramo in tramos_impuesto:
        
        # Ignoramos los tramos exentos para este ejemplo
        if tramo["Desde"] != "-" and tramo["Hasta"] != "Y MÁS":
            desde_numerico = float(tramo["Desde"].replace("$ ", "").replace(".", "").replace(",", "."))
            hasta_numerico = float(tramo["Hasta"].replace("$ ", "").replace(".", "").replace(",", "."))
            if desde_numerico < sueldo_antes_impuesto <= hasta_numerico:
                print(f"Para un monto de {sueldo_antes_impuesto}, el tramo es: {tramo}")
                tasa = float(tramo["Factor"])
                rebaja = float(tramo["Cantidad a Rebajar"].replace("$ ", "").replace(".", "").replace(",", "."))

                break
    impuesto_seg_categoria = sueldo_antes_impuesto * tasa - rebaja
    sueldo_despues_impuesto = sueldo_antes_impuesto - impuesto_seg_categoria

    datos_liquidacion['tasa'] = tasa
    datos_liquidacion['rebaja'] = rebaja
    datos_liquidacion['sueldo_despues_impuesto'] = sueldo_despues_impuesto

    contexto = {'form': form, **datos_liquidacion}
    return render(request, 'liquidacion.html', contexto)
