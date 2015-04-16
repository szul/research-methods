USE [Research.Active.001]
GO

/****** Object:  Table [User].[Person]    Script Date: 4/16/2015 1:58:10 PM ******/
DROP TABLE [User].[Person]
GO

/****** Object:  Table [User].[Person]    Script Date: 4/16/2015 1:58:10 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [User].[Person](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Active] [bit] NOT NULL CONSTRAINT [DF_User_Person_Active]  DEFAULT ((1)),
	[Hidden] [bit] NOT NULL CONSTRAINT [DF_User_Person_Hidden]  DEFAULT ((0)),
	[ReadOnly] [bit] NOT NULL CONSTRAINT [DF_User_Person_ReadOnly]  DEFAULT ((0)),
	[DateCreated] [datetime] NOT NULL CONSTRAINT [DF_User_Person_DateCreated]  DEFAULT (getdate()),
	[DateModified] [datetime] NOT NULL CONSTRAINT [DF_User_Person_DateModified]  DEFAULT (getdate()),
	[US] [uniqueidentifier] NULL,
	[RS] [uniqueidentifier] NOT NULL CONSTRAINT [DF_User_Person_RS]  DEFAULT (newid()),
	[Meta] [xml] NULL,
	[Code] [nvarchar](50) NULL,
	[Name] [nvarchar](200) NOT NULL,
	[Description] [nvarchar](2000) NULL,
	[TS] [timestamp] NOT NULL,
	[Email] [nvarchar](100) NOT NULL,
	[Password] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_Person_1] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO


