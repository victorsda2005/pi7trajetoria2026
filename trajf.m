function q = trajf(pos)
    x = pos(1);
    y = pos(2);
    parameters = params();
    l1=parameters(1);
    l2=parameters(2);
    l3=parameters(3);
    l0=l3/2;
    yoffset = parameters(4);
    alpha1_calc = (l1^2 + (((l0+x)^2)+(y-yoffset)^2)-l2^2)/(2*l1*sqrt((l0+x)^2+(y-yoffset)^2));
    alpha2_calc = (l1^2 + (((l0-x)^2)+(y-yoffset)^2)-l2^2)/(2*l1*sqrt((l0-x)^2+(y-yoffset)^2));

    if alpha1_calc > 1 || alpha2_calc > 1
        display("coordenadas não alcançáveis")
        return
    end

    alpha1 = acos(alpha1_calc);
    alpha2 = acos(alpha2_calc);
    %beta1 = atan((y-yoffset)/(l0+x));
    %beta2 = atan((y-yoffset)/(l0-x));
    beta1 = atan2((y-yoffset),(l0+x));
    beta2 = atan2((y-yoffset),(l0-x));
    q(1) = beta1+alpha1;
    q(2) = pi-beta2-alpha2;
end
