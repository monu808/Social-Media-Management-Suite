# 🚀 Social Media Management Suite - MCP Server

A comprehensive **Model Context Protocol (MCP)** server that provides AI-powered social media management tools. This server enables automated content creation, scheduling, analytics, competitor analysis, and hashtag optimization across multiple platforms.

## 🌟 Features

### 📱 Core Social Media Tools
- **Post Scheduling** - Schedule posts across Twitter, Instagram, Facebook, LinkedIn
- **Hashtag Generation** - AI-powered hashtag suggestions with trending analysis
- **Analytics & Insights** - Comprehensive engagement metrics and audience analytics
- **Trending Topics** - Real-time trend tracking with content ideas
- **Content Management** - View and manage scheduled posts

### 🤖 AI-Powered Enhanced Tools
- **Content Suggestions** - AI-generated content ideas optimized for each platform
- **Content Calendar** - Strategic content planning with AI recommendations
- **Audience Insights** - Detailed demographics and engagement analysis
- **Competitor Analysis** - Track and analyze competitor strategies
- **Advanced Hashtags** - Smart hashtag optimization with difficulty scoring

### 🔧 Technical Features
- **Multi-platform Support** - Twitter, Instagram, Facebook, LinkedIn
- **Real-time API Integration** - Connect with actual social media APIs
- **Data Persistence** - Intelligent caching and data management
- **Secure Authentication** - Token-based security for API access
- **Scalable Architecture** - Built with FastMCP for high performance

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- ngrok (for external access)
- API keys for social media platforms (optional)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/monu808/Social-Media-Management-Suite.git
cd Social-Media-Management-Suite/social-media-mcp-server
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:

```env
# MCP Authentication
AUTH_TOKEN=your_auth_token_here
MY_NUMBER=your_phone_number_here

# Twitter/X API (Optional)
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# Facebook/Instagram API (Optional)
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token

# LinkedIn API (Optional)
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret

# AI Services (Optional)
OPENAI_API_KEY=your_openai_api_key
RITEKIT_API_KEY=your_ritekit_api_key

# Analytics Services (Optional)
HOOTSUITE_API_KEY=your_hootsuite_api_key
```

### 4. Start the Server
```bash
python mcp_social_server.py
```

The server will start on `http://0.0.0.0:8086`

### 5. Set Up External Access (Optional)
For external access via Puch AI or other MCP clients:

```bash
ngrok http 8086
```

## 🎯 Usage

### Basic Commands

#### Schedule a Post
```python
await schedule_post(
    content="Your post content here",
    platforms="twitter,instagram",
    schedule_time="2024-12-25 14:30",
    media_url="https://example.com/image.jpg"  # optional
)
```

#### Generate Hashtags
```python
await generate_hashtags(
    content="Your post content",
    platform="instagram",
    count=10
)
```

#### Get Analytics
```python
await get_analytics(
    platform="all",
    timeframe="30d",
    metric_type="engagement"
)
```

#### Create Content Suggestions
```python
await create_content_suggestion(
    platform="instagram",
    content_type="engagement",
    topic="technology"
)
```

### Available MCP Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `schedule_post` | Schedule posts across platforms | content, platforms, schedule_time, media_url |
| `generate_hashtags` | Generate relevant hashtags | content, platform, count |
| `get_analytics` | Get engagement metrics | platform, timeframe, metric_type |
| `get_trending_topics` | Track trending topics | platform, category, location |
| `manage_scheduled_posts` | Manage scheduled posts | action, post_id |
| `create_content_suggestion` | AI content suggestions | platform, content_type, topic |
| `create_content_calendar` | Strategic content planning | platform, days, focus_topics |
| `get_audience_insights` | Audience analytics | platform, insight_type |
| `manage_competitors` | Competitor analysis | action, competitor_name, platforms |
| `generate_advanced_hashtags` | Advanced hashtag optimization | content, platform, count, strategy |

## 🔌 Integration

### With Puch AI (WhatsApp)
1. Start your server and ngrok
2. Get your ngrok URL: `https://your-ngrok-url.ngrok-free.app`
3. In WhatsApp, send:
   ```
   /mcp use https://your-ngrok-url.ngrok-free.app/mcp/ your_auth_token
   ```

### With Other MCP Clients
Connect to `http://your-server:8086/mcp/` with your authentication token.

## 📁 Project Structure

```
social-media-mcp-server/
├── mcp_social_server.py     # Main MCP server
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── data/                 # Data storage
│   ├── scheduled_posts.json
│   ├── analytics_cache.json
│   └── trends_cache.json
└── utils/                # Utility modules
    ├── __init__.py
    ├── data_manager.py
    ├── social_apis.py
    ├── hashtag_engine.py
    ├── content_creator.py
    ├── audience_insights.py
    └── competitor_analysis.py
```

## 🔑 API Keys Setup

### Twitter/X API
1. Create a Twitter Developer account
2. Create a new app and get your credentials
3. Add to `.env` file

### OpenAI API
1. Sign up at OpenAI
2. Generate an API key
3. Add `OPENAI_API_KEY` to `.env`

### Other APIs
- **Facebook/Instagram**: Meta Developer Platform
- **LinkedIn**: LinkedIn Developer Network
- **RiteKit**: Hashtag optimization service

## 🚨 Troubleshooting

### Common Issues

**Server Not Starting**
- Check Python version (3.8+)
- Install dependencies: `pip install -r requirements.txt`
- Verify port 8086 is available

**MCP Connection Failed**
- Ensure server is running on correct port
- Check ngrok tunnel is active
- Verify authentication token matches

**Missing Utility Modules**
- All utility modules are included
- Check for import errors in logs
- Server works with mock data if modules fail

### Debug Mode
Add debugging to your `.env`:
```env
DEBUG=true
LOG_LEVEL=debug
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **FastMCP Documentation**: [https://gofastmcp.com](https://gofastmcp.com)
- **MCP Specification**: [https://spec.modelcontextprotocol.io](https://spec.modelcontextprotocol.io)
- **Puch AI**: Connect via WhatsApp for easy access

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review server logs for error details

---

**Built with ❤️ using FastMCP and Python**

*Empowering social media management through AI and automation*
