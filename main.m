% Projet de Maintenance Prédictive (Version MATLAB)
% Ce script reproduit la logique du projet Python pour la prédiction de pannes.

%% 1. Chargement et Nettoyage des Données
disp('--- Chargement des données ---');
filename = 'machine failure.csv';
opts = detectImportOptions(filename);
opts.SelectedVariableNames = {'Type', 'AirTemperature_K_', 'ProcessTemperature_K_', ...
                              'RotationalSpeed_rpm_', 'Torque_Nm_', 'ToolWear_min_', 'MachineFailure'};
data = readtable(filename, opts);

% Conversion de la colonne 'Type' (L, M, H) en numérique (1, 2, 3)
data.Type = grp2idx(data.Type);

% Séparation Features (X) et Target (Y)
% Features: Type, Temperatures, Speed, Torque, ToolWear
X = [data.Type, data.AirTemperature_K_, data.ProcessTemperature_K_, ...
     data.RotationalSpeed_rpm_, data.Torque_Nm_, data.ToolWear_min_]'; % Transposé pour MATLAB (Features x Samples)

% Target: MachineFailure
Y = data.MachineFailure'; % Transposé (1 x Samples)

%% 2. Création et Entraînement du Réseau de Neurones
disp('--- Entraînement du Réseau de Neurones (patternnet) ---');

% Création d'un réseau de reconnaissance de motifs (Pattern Recognition)
% 2 couches cachées de 100 et 50 neurones (identique à Python)
hiddenLayerSize = [100, 50];
net = patternnet(hiddenLayerSize);

% Division des données : 70% Train, 15% Validation, 15% Test
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;

% Entraînement
[net, tr] = train(net, X, Y);

%% 3. Évaluation
disp('--- Évaluation ---');

% Prédiction sur les données de test
XTest = X(:, tr.testInd);
YTest = Y(:, tr.testInd);
YPred = net(XTest);

% Conversion des probabilités en classes (0 ou 1)
YPredClass = round(YPred);

% Calcul de la précision (Accuracy)
accuracy = sum(YPredClass == YTest) / length(YTest);
fprintf('Précision sur le jeu de test : %.2f%%\n', accuracy * 100);

% Affichage de la Matrice de Confusion
figure;
plotconfusion(YTest, YPred);
title('Matrice de Confusion (MATLAB)');
