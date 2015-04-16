USE [Research.In.001]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_RS]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_DateModified]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_DateCreated]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_ReadOnly]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_Hidden]
GO

ALTER TABLE [User].[Data] DROP CONSTRAINT [DF_User_Data_Active]
GO

/****** Object:  Table [User].[Data]    Script Date: 4/16/2015 1:58:23 PM ******/
DROP TABLE [User].[Data]
GO

/****** Object:  Table [User].[Data]    Script Date: 4/16/2015 1:58:23 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [User].[Data](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Active] [bit] NOT NULL,
	[Hidden] [bit] NOT NULL,
	[ReadOnly] [bit] NOT NULL,
	[DateCreated] [datetime] NOT NULL,
	[DateModified] [datetime] NOT NULL,
	[US] [uniqueidentifier] NULL,
	[RS] [uniqueidentifier] NOT NULL,
	[Meta] [xml] NULL,
	[Code] [nvarchar](50) NULL,
	[Name] [nvarchar](200) NOT NULL,
	[Description] [nvarchar](2000) NULL,
	[TS] [timestamp] NOT NULL,
	[JSON] [text] NULL,
 CONSTRAINT [PK_Data_1] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_Active]  DEFAULT ((1)) FOR [Active]
GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_Hidden]  DEFAULT ((0)) FOR [Hidden]
GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_ReadOnly]  DEFAULT ((0)) FOR [ReadOnly]
GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_DateCreated]  DEFAULT (getdate()) FOR [DateCreated]
GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_DateModified]  DEFAULT (getdate()) FOR [DateModified]
GO

ALTER TABLE [User].[Data] ADD  CONSTRAINT [DF_User_Data_RS]  DEFAULT (newid()) FOR [RS]
GO


