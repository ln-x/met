dt = 60
dx = 500
U = 0.533915246466
T_sed = 19.5695044457 #ground[1]
T_prev = 19.5380274571
Q_hyp = 0.00527999213552
Q_tup = () #Q tributaries
T_tup = () #WT tributaries
Q_up = 0.527999237393 #Q_up_prev
Delta_T = -0.00140320204542 #current temperature calculated only from local fluxes (in: __init__ of class StramNode)
Disp = 25.6718013187
S1 = True
S1_value =  -1.9072624939e-05
T0 = 19.5402327424 #T_up_prev, prev_km.T
T1 = 19.5368830996 #T_prev, T
T2 = 19.5374935198 #T_dn_prev, next_km.T
Q_accr = 0
T_accr = 0
MixTDelta_dn = 0.000311685654754 #MixTDelta_dn_prev, Mix_T_Delta: Change in temp. due to trib, gw, point sources, accr.

#called by function CalcHeatFluxes
def CalcMacCormick(dt, dx, U, T_sed, T_prev, Q_hyp, Q_tup, T_tup, Q_up, Delta_T, Disp, S1,
                   S1_value, T0, T1, T2, Q_accr, T_accr, MixTDelta_dn):
    Q_in = 0
    T_in = 0
    T_up = T0
    numerator = 0
    for i in xrange(len(Q_tup)):
        Qitem = Q_tup[i]
        Titem = T_tup[i]

        if Qitem is None or (Qitem > 0 and Titem is None): # value for discharge? T can be blank if discharge is neg. (withdrawl)
            raise HeatSourceError("Problem with null value in tributary discharge or temperature")
        if Qitem > 0:
            Q_in += Qitem
            numerator += Qitem*Titem
    if numerator and (Q_in > 0):
        T_in = numerator/Q_in
    T_mix = 0 #TODO: test - skip all tribuary mixing to only calculate temperature change caused by Delta_T/dt
    #T_mix = ((Q_in * T_in) + (T_up * Q_up)) / (Q_up + Q_in)
    #T_mix = ((T_sed * Q_hyp) + (T_mix * (Q_up + Q_in))) / (Q_hyp + Q_up + Q_in) #hyporheic exchange
    #T_mix = ((Q_accr * T_accr) + (T_mix * (Q_up + Q_in + Q_hyp))) / (Q_accr + Q_up + Q_in + Q_hyp) #accretion
    #T_mix -= T_up
    #T0 += T_mix #adjust upstream temperature by tributary mixing
    #T2 -= MixTDelta_dn #adjust downstream temperature to account for mixing

    Dummy1 = -U * (T1 - T0) / dx
    Dummy2 = Disp * (T2 - 2 * T1 + T0) / (dx**2)
    print "Dummy1 %d, Dummy2 %d" %(Dummy1, Dummy2)
    S = Dummy1 +  Dummy2 + Delta_T / dt
    if S1:                                              #if SI = True (nearly always vs. in CalcHeatFluxes set to 0)
        Temp = T_prev + ((S1_value + S) / 2) * dt
    else:
        Temp = T1 + S * dt
    return Temp, S, T_mix

Temp, S, T_mix =  CalcMacCormick(dt, dx, U, T_sed, T_prev, Q_hyp, Q_tup, T_tup, Q_up, Delta_T, Disp, S1,
                   S1_value, T0, T1, T2, Q_accr, T_accr, MixTDelta_dn)

print Temp, S, T_mix
#output: 19.5368823993 -1.90959703007e-05 0.000289818831227 OK :-)

def CalcHeatFluxes(ContData, C_args, d_w, area, P_w, W_w, U, Q_tribs, T_tribs, T_prev,
                   T_sed, Q_hyp, T_dn_prev, ShaderList, Disp, hour, JD, daytime, Altitude, Zenith,
                   Q_up_prev, T_up_prev, solar_only, MixTDelta_dn_prev):
    #ground = GetGroundFluxes(...., T_prev, ...)
    F_Total =  solar[6] + ground[0] + ground[2] + ground[6] + ground[7]
    Delta_T = F_Total * dt / ((area / W_w) * 4182 * 998.2) # Vars are Cp (J/kg *C) and P (kgS/m3)
    Mac = CalcMacCormick(dt, dx, U, ground[1], T_prev, Q_hyp, Q_tribs, T_tribs, Q_up_prev,
                Delta_T, Disp, 0, 0.0, T_up_prev, T_prev, T_dn_prev, Q_accr, T_accr, MixTDelta_dn_prev)
    #Mac includes Temp, S, T_mix
    return solar, ground, F_Total, Delta_T, Mac, veg_block

 def CalcHeat_Opt(self, time, hour, min, sec, JD, JDC, solar_only=False):
        self.T_prev = self.T
        self.T = None
        try:
            if not self.hydro_used:
                self.F_Solar, ground, self.F_Total, self.Delta_T, (self.T, self.S1, self.Mix_T_Delta), \
                    veg_block = \
                    _HS.CalcHeatFluxes(self.ContData[time], self.C_args, self.d_w, self.A, self.P_w, self.W_w, self.U,
                                self.Q_tribs[time], self.T_tribs[time], self.T_prev, self.T_sed,
                                self.Q_hyp,self.next_km.T_prev, self.ShaderList[dir], self.Disp,
                                hour, JD, Daytime,Altitude, Zenith, self.prev_km.Q_prev, self.prev_km.T_prev,
                                solar_only, self.next_km.Mix_T_Delta)
            ...

