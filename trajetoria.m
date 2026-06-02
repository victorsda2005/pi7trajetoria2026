n = 100;
x = linspace(-100, 200, n);
y = linspace(200, 100, n);
theta= linspace(pi/4,3*pi/4,n);
r=300;
traj = [x;y];
traj2= [r*cos(theta);r*sin(theta)];

q_sol = zeros(2,n);
parameters = params();
l1=parameters(1);
l2=parameters(2);
l3=parameters(3);
l0=l3/2;
yoffset = parameters(4);
%traj = traj2;
for i=1:n
    q_sol(:,i) = trajf(traj(:,i));
end
hold on
grid on
axis([-l0*1.5,l0*1.5,-100+yoffset,600+yoffset]);
axis equal
r1 = l1+l2;
r2 = l1-l2;
c1 = circle(-l3/2, yoffset, r1);
c2 = circle(l3/2, yoffset, r1);
c3 = circle(-l3/2, yoffset, r2);
c4 = circle(l3/2, yoffset, r2);
A=[-l0, yoffset];
B=[l0, yoffset];
plot(A(1), A(2), 'ok')
plot(B(1), B(2), 'ok')
plot(traj(1,:),traj(2,:), '--b', 'LineWidth',2)
%exportgraphics(gcf,"teste.gif");
for k=1:n
    t = plot_mec(q_sol(:,k),traj(:,k));
    if k == 1 
        exportgraphics(gcf,"teste.gif");
    end
    exportgraphics(gcf,"teste.gif","Append",true);
    size_ = length(t);
    for i=1:size_
        delete(t(i))
    end
    %plot([l0,Ax_plot],[0,Ay_plot], '-ok',[Ax_plot,Cx_plot], [Ay_plot,Cy_plot], '-ok')
    %plot([-l0,Bx_plot],[0,By_plot], '-ok',[Bx_plot,Cx_plot], [By_plot,Cy_plot], '-k')
    %plot(Cx_plot, Cy_plot, 'b*')
end

hold off
