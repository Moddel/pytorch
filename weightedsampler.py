# an example to use torch.utils.data.sampler.WeightedRandomSampler
# from link: https://discuss.pytorch.org/t/how-to-prevent-overfitting/1902/5

batch_size = 20
class_sample_count = [10, 1, 20, 3, 4] # dataset has 10 class-1 samples, 1 class-2 samples, etc.
weights = 1 / torch.Tensor(class_sample_count)
weights = weights.double()
sampler = torch.utils.data.sampler.WeightedRandomSampler(weights, batch_size)
trainloader = data_utils.DataLoader(train_dataset, batch_size = batch_size, shuffle=True, sampler = sampler)
