function f = plot_mec(q, traj)
    x = traj(1);
    y = traj(2);
    parameters = params();
    l1=parameters(1);
    l2=parameters(2);
    l3=parameters(3);
    yoffset = parameters(4);
    l0=l3/2;
    A=[-l0, yoffset];
    B=[l0, yoffset];
    C=A+l1*[cos(q(1)), sin(q(1))];
    D=B+l1*[cos(q(2)), sin(q(2))];
    E=[x,y];
    %plot(A(1), A(2), 'ok')
    %plot(B(1), B(2), 'ok')
    f(1) = plot(E(1), E(2), 'or');
    f(2) = plot([A(1), C(1)], [A(2), C(2)], '-ok');
    f(3) = plot([B(1), D(1)], [B(2), D(2)], '-ok');
    f(4) = plot([C(1), E(1)], [C(2), E(2)], '-k');
    f(5) = plot([E(1), D(1)], [E(2), D(2)], '-k');
end
