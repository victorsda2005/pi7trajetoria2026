clc, clear, close all

%% Parâmetros

R = 300;

function res = coef_polinomio(tf)

A = [1*tf^5 1*tf^4  1*tf^3;
  5*tf^4 4*tf^3  3*tf^2;
  20*tf^3 12*tf^2 6*tf];

b = [1; 0; 0];
res = A\b;
end

%% Polinômio Reta

tf_reta = 15;
n_reta = 10;
t_reta =  linspace(0, tf_reta, n_reta);
coef_reta = coef_polinomio(tf_reta);

tau_reta = coef_reta(1)*t_reta.^5 + coef_reta(2)*t_reta.^4 + coef_reta(3)*t_reta.^3;

%% Polinômio Curva

tf_curva = 8;
n_curva = 50;
t_curva =  linspace(0, tf_curva, n_curva);
coef_curva = coef_polinomio(tf_curva);

tau_curva = coef_curva(1)*t_curva.^5 + coef_curva(2)*t_curva.^4 + coef_curva(3)*t_curva.^3;

%% Reta

xreta = 300*tau_reta - 100;
yreta = -100*tau_reta + 200;

%% Curva

theta = 3*pi/4 - pi*tau_curva/2;
xcurva = R * cos(theta);
ycurva = R * sin(theta);

%% Doidera

traj1 = [xreta;yreta];
traj2 = [xcurva;ycurva];

traj = traj1;
n = n_reta;

%traj = traj2;
%n = n_curva;

q_sol = zeros(2,n);
parameters = params();
l1=parameters(1);
l2=parameters(2);
l3=parameters(3);
l0=l3/2;
yoffset = parameters(4);
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
plot(traj(1,:),traj(2,:), '--b', 'LineWidth',2,'Marker','o','MarkerFaceColor','blue','MarkerEdgeColor','black')
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
