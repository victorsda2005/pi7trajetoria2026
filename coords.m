function pos = coords(q)
    parameters = params();
    l1=parameters(1);
    l2=parameters(2);
    l3=parameters(3);
    l0=l3/2;
    yoffset = parameters(4);
    m = l3+l1*(cos(q(2))-cos(q(1)));
    h = sin(q(1))-sin(q(2));
    n = l1*abs(h);
    psi = atan(n/m);
    phi = acos((sqrt(n^2+m^2))/(2*l2));
    theta4 = phi+psi;
    theta3 = pi-phi+psi;
    x = -l0+l1*cos(q(1))+l2*cos(theta4);
    y = yoffset+l1*sin(q(1))+l2*sin(theta4);
    x2= l0+l1*cos(q(2))+l2*cos(theta3);
    y2= yoffset+l1*sin(q(2))+l2*sin(theta3);
    if (abs(x-x2) > 0.1) || (abs(y-y2) > 0.1)
        theta4 = 2*pi-phi+psi;
        theta3 = pi+phi+psi;
    else
        pos = [x,y];
        return
    end
    x = -l0+l1*cos(q(1))+l2*cos(theta4);
    y = yoffset+l1*sin(q(1))+l2*sin(theta4);
    x2= l0+l1*cos(q(2))+l2*cos(theta3);
    y2= yoffset+l1*sin(q(2))+l2*sin(theta3);
    if (abs(x-x2) > 0.1) || (abs(y-y2) > 0.1)
        pos = [0,0]; %erro
    else
        pos = [x,y];
    end
end
