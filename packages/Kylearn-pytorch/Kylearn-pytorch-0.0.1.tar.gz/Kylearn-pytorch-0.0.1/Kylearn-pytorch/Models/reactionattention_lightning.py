import pytorch_lightning as pl


# class ReactionModelLightning(pl.LightningModule):
#     def __init__(self, dataloader, stack, d_reactant, d_bottleneck, d_classifier, d_output, threshold=None,
#                  n_layers=6, n_head=8, dropout=0.1):
#         super().__init__()
#
#         self.dataloader = dataloader
#         feature1_dim, feature2_dim = self.dataloader.get_feature_dim()
#         self.model = stack(n_layers, n_head, feature1_dim, feature2_dim, d_reactant, d_bottleneck,
#                            dropout)
#         self.fc1 = nn.Linear(feature1_dim, d_classifier)
#         self.fc2 = nn.Linear(d_classifier, d_output)
#
#         self.d_output = d_output
#         self.threshold = threshold
#
#     def forward(self, feature_1, feature_2):
#         output = self.model(feature_1, feature_2)
#         output = self.fc1(output[0])
#         output = nn.functional.relu(output)
#         output = self.fc2(output)
#         return output
#
#     def training_step(self, batch, batch_nb):
#         feature_1, feature_2, y = batch
#         logits = self.forward(feature_1, feature_2)
#         pred = logits.sigmoid()
#
#         if y.shape[-1] == 1:
#             loss = mse_loss(pred, y)
#
#         else:
#             loss = cross_entropy_loss(pred, y, smoothing=True)
#
#         acc = accuracy(pred, y, threshold=self.threshold)
#         _, _, precision_avg, recall_avg = precision_recall(pred, y, self.d_output, threshold=self.threshold)
#         tensorboard_logs = {'train_loss': loss, 'train_acc': acc,
#                             'train_precision': precision_avg,
#                             'train_recall': recall_avg}
#
#         return {'loss': loss, 'acc': acc, 'precision': precision_avg, 'recall': recall_avg, 'log': tensorboard_logs}
#
#     def validation_step(self, batch, batch_nb):
#         feature_1, feature_2, y = batch
#         logits = self.forward(feature_1, feature_2)
#         pred = logits.sigmoid()
#
#         if y.shape[-1] == 1:
#             loss = mse_loss(pred, y)
#
#         else:
#             loss = cross_entropy_loss(pred, y, smoothing=False)
#
#         acc = accuracy(pred, y, threshold=self.threshold)
#         _, _, precision_avg, recall_avg = precision_recall(pred, y, self.d_output, threshold=self.threshold)
#
#         return {'val_loss': loss, 'val_acc': acc,
#                 'val_precision': precision_avg,
#                 'val_recall': recall_avg}
#
#     def validation_end(self, outputs):
#         avg_loss = torch.stack([x['val_loss'] for x in outputs]).mean()
#         avg_acc = torch.stack([x['val_acc'] for x in outputs]).mean()
#         avg_precision = torch.stack([x['val_precision'] for x in outputs]).mean()
#         avg_recall = torch.stack([x['val_recall'] for x in outputs]).mean()
#
#         tensorboard_logs = {'val_loss': avg_loss, 'val_acc': avg_acc,
#                             'val_precision': avg_precision,
#                             'val_recall': avg_recall}
#
#         return {'loss': avg_loss, 'acc': avg_acc, 'precision': avg_precision, 'recall': avg_recall,
#                 'log': tensorboard_logs}
#
#     def configure_optimizers(self):
#         # return AdamOptimizer(self.parameters(), 1000, 0.01)
#         return Adam(self.parameters(), lr=0.005, betas=(0.9, 0.999))
#
#     @pl.data_loader
#     def train_dataloader(self):
#         return self.dataloader.train_dataloader()
#
#     @pl.data_loader
#     def val_dataloader(self):
#         return self.dataloader.val_dataloader()
#
#     @pl.data_loader
#     def test_dataloader(self):
#         return self.dataloader.test_dataloader()