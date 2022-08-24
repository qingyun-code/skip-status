import torch
import torch.nn as nn

class net(nn.Module):
	def __init__(self):
		super(net, self).__init__()

		self.Conv_layers1 = nn.Sequential(
				nn.Conv2d(3, 128, 12, 2),
				nn.LeakyReLU(),
				nn.MaxPool2d(2, 2)
			)

		self.Conv_layers2 = nn.Sequential(
				nn.Conv2d(128, 256, 6, 2),
				nn.LeakyReLU(),
				nn.MaxPool2d(2, 2)
			)

		self.Conn_layers1 = nn.Sequential(
				nn.Linear(14 * 14 * 256, 1000),
				nn.LeakyReLU()
			)

		self.Conn_layers2 = nn.Sequential(
				nn.Linear(1000, 3),
				nn.Sigmoid()
			)

	def forward(self, input):
		input = self.Conv_layers1(input)
		input = self.Conv_layers2(input)
		input = input.view(input.size()[0], -1)
		input = self.Conn_layers1(input)
		input = self.Conn_layers2(input)
		output = input.reshape(-1, 3)

		return output