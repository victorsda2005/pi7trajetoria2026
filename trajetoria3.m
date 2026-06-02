
clc, clear, close all

%% Parâmetros

R = 300;
debug = 0;

function res = reta_polinomio(dt,n,p0,p1)
%acha um polinômio de p0 até p1 com passo dt e n pontos

A = [1*dt^5 1*dt^4  1*dt^3;
  5*dt^4 4*dt^3  3*dt^2;
  20*dt^3 12*dt^2 6*dt];
x1 = p1(1);
x0 = p0(1);
y1 = p1(2);
y0 = p0(2);
bx = [x1-x0; 0; 0];
by = [y1-y0; 0; 0];
coefx = A\bx;
coefy = A\by;
t_vec = linspace(0,dt,n);
x = x0+coefx(1)*t_vec.^5 + coefx(2)*t_vec.^4 + coefx(3)*t_vec.^3;
y = y0+coefy(1)*t_vec.^5 + coefy(2)*t_vec.^4 + coefy(3)*t_vec.^3;
res = [x;y];
end

%% Polinômio Reta

n_pontos = 10; %numero de pontos em cada reta (min. 3)

%% Reta

ini = [-100,200];
fim = [200,100];
tempo=15; %tempode para fazer a reta
traj_reta=(reta_polinomio(tempo,n_pontos,ini,fim));

%% Curva

n_reta = 5; %numero de retas que definem a trajetoria (min. 2)
theta = linspace(3*pi/4, pi/4, n_reta+1);
xcurva = R * cos(theta);
ycurva = R * sin(theta);
traj_circ = [xcurva;ycurva];
tempo = 8; %tempo de fazer o circulo
traj_polig = zeros(2,(n_pontos - 1)*n_reta + 1);
for i=1:n_reta
  s = 1+(i-1)*(n_pontos-1);
  f = 1+i*(n_pontos-1);
  traj_polig(:,s:f) = reta_polinomio(tempo/n_reta,n_pontos,traj_circ(:,i),traj_circ(:,i+1));
end
if debug==1
  parameters = params();
  l3=parameters(3);
  l0=l3/2;
  yoffset = parameters(4);
  figure
  plot(traj_reta(1,:),traj_reta(2,:))
  axis([-l0*1.5,l0*1.5,-100+yoffset,600+yoffset]);
  axis equal
  figure
  plot(traj_circ(1,:),traj_circ(2,:))
  axis([-l0*1.5,l0*1.5,-100+yoffset,600+yoffset]);
  axis equal
  figure
  plot(traj_polig(1,:),traj_polig(2,:))
  axis([-l0*1.5,l0*1.5,-100+yoffset,600+yoffset]);
  axis equal
end

traj = traj_reta;
%traj = traj_polig;
[~,n] = size(traj);

%% Desenha mecanismo percorrendo trajetoria

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
figure
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
