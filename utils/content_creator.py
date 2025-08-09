#!/usr/bin/env python3
"""
Content Creator Utility
AI-powered content creation for social media platforms.
"""

import os
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

class ContentCreator:
    """Handles AI-powered content creation and suggestions."""
    
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.content_templates = self._load_content_templates()
    
    def _load_content_templates(self) -> Dict[str, List[str]]:
        """Load content templates for different platforms and types."""
        return {
            "instagram": {
                "engagement": [
                    "🔥 What's your favorite {topic} story? Drop it in the comments! 👇",
                    "✨ {topic} fact: Did you know... Share if this blew your mind! 🤯",
                    "💭 If you could experience one {topic} adventure, which would it be?",
                    "🎨 Tag someone who loves {topic} as much as you do! 💫",
                    "🌟 Double tap if {topic} fascinates you! What draws you to it?"
                ],
                "informative": [
                    "📚 {topic} Deep Dive: Let's explore the fascinating world of...",
                    "🔍 Breaking down {topic}: Here's what you need to know...",
                    "💡 {topic} Explained: Understanding the basics and beyond...",
                    "📖 The Ultimate {topic} Guide: Everything you've ever wondered...",
                    "🎓 {topic} 101: Your beginner's guide to understanding..."
                ],
                "promotional": [
                    "🚀 Ready to dive deeper into {topic}? Check out our latest...",
                    "💯 Loving {topic}? You'll absolutely adore this...",
                    "✨ For all {topic} enthusiasts, we've got something special...",
                    "🔥 New {topic} content alert! Don't miss out on...",
                    "🎯 {topic} lovers, this one's for you! Discover..."
                ],
                "trending": [
                    "🔥 Everyone's talking about {topic} right now! Here's why...",
                    "📈 {topic} is trending and we're here for it! Let's discuss...",
                    "💫 Joining the {topic} conversation with our take on...",
                    "🌟 The {topic} trend explained: What it means and why it matters...",
                    "⚡ Riding the {topic} wave! Here's our perspective on..."
                ]
            },
            "twitter": {
                "engagement": [
                    "Hot take on {topic}: [Your opinion here] What do you think? 🧵",
                    "Quick {topic} poll: Which side are you on? Vote below! 👇",
                    "Unpopular {topic} opinion: [Share your take] Change my mind 💭",
                    "{topic} enthusiasts, assemble! What's your favorite aspect? 🔥",
                    "Real talk about {topic}: [Your insight] Who agrees? 🙋"
                ],
                "informative": [
                    "🧵 {topic} thread: Everything you need to know (1/n)",
                    "Breaking: New developments in {topic} that will change everything",
                    "📊 {topic} by the numbers: Here are the facts that matter",
                    "💡 {topic} tip of the day: [Share valuable insight]",
                    "🔍 Deep dive into {topic}: The complete breakdown"
                ],
                "promotional": [
                    "🚀 Launching our new {topic} resource! Check it out: [link]",
                    "📢 Attention {topic} fans! We've got something special for you",
                    "💯 Our {topic} guide just dropped! Everything you need: [link]",
                    "🎯 For {topic} lovers: Don't miss our latest update",
                    "✨ New {topic} content is live! Dive in: [link]"
                ],
                "trending": [
                    "Why {topic} is trending and what it means for you 🧵",
                    "Joining the {topic} conversation with our take 👇",
                    "The {topic} trend explained in under 60 seconds ⏰",
                    "Everyone's talking {topic} - here's our perspective 💭",
                    "Breaking down the {topic} phenomenon 📈"
                ]
            },
            "linkedin": {
                "engagement": [
                    "What's your experience with {topic}? I'd love to hear your insights in the comments.",
                    "Here's an interesting perspective on {topic}. What are your thoughts?",
                    "I've been reflecting on {topic} lately. What challenges have you faced?",
                    "Let's discuss {topic}: What trends are you seeing in your industry?",
                    "Curious about your take on {topic}. How has it impacted your work?"
                ],
                "informative": [
                    "5 key insights about {topic} that every professional should know",
                    "The future of {topic}: What to expect in the next 5 years",
                    "How {topic} is transforming the way we work: A comprehensive analysis",
                    "Understanding {topic}: A guide for business leaders",
                    "The impact of {topic} on modern workplace dynamics"
                ],
                "promotional": [
                    "Excited to share our latest insights on {topic}. Check out our new resource:",
                    "We've been working on something special for {topic} professionals:",
                    "Proud to announce our new {topic} initiative. Learn more:",
                    "For those interested in {topic}, we've created a comprehensive guide:",
                    "Our team has been researching {topic}. Here's what we found:"
                ],
                "trending": [
                    "Why {topic} is dominating industry conversations right now",
                    "The {topic} trend: What it means for business leaders",
                    "Breaking down the {topic} phenomenon and its implications",
                    "How the {topic} movement is reshaping our industry",
                    "Understanding the {topic} trend: Opportunities and challenges"
                ]
            }
        }
    
    async def get_content_suggestion(self, platform: str, content_type: str, topic: str) -> Dict[str, Any]:
        """Generate content suggestions for the specified platform and type."""
        try:
            # Try AI-powered generation first if OpenAI key is available
            if self.openai_api_key:
                try:
                    return await self._generate_ai_content(platform, content_type, topic)
                except Exception as e:
                    print(f"AI generation failed: {e}")
                    # Fall back to template-based generation
            
            # Template-based generation
            return self._generate_template_content(platform, content_type, topic)
            
        except Exception as e:
            return {"error": f"Failed to generate content: {str(e)}"}
    
    async def _generate_ai_content(self, platform: str, content_type: str, topic: str) -> Dict[str, Any]:
        """Generate content using OpenAI API."""
        try:
            from openai import OpenAI
            
            client = OpenAI(api_key=self.openai_api_key)
            
            platform_guidelines = {
                "instagram": "Visual, engaging, use emojis, hashtag-friendly, storytelling",
                "twitter": "Concise, conversational, thread-worthy, trending-aware",
                "linkedin": "Professional, insightful, business-focused, thought leadership",
                "facebook": "Community-focused, shareable, conversation-starting"
            }
            
            prompt = f"""Create 3 {content_type} social media posts for {platform} about {topic}.

Platform guidelines: {platform_guidelines.get(platform, "Engaging and relevant")}

Requirements:
- Make them {content_type} and engaging
- Include relevant emojis where appropriate
- Keep platform character limits in mind
- Make them actionable and shareable
- Focus on {topic}

Return 3 different post ideas, each on a new line."""
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.8
            )
            
            suggestions = response.choices[0].message.content.strip().split('\n')
            suggestions = [s.strip() for s in suggestions if s.strip()]
            
            return {
                "suggestions": suggestions[:3],
                "platform": platform,
                "content_type": content_type,
                "topic": topic,
                "generated_by": "openai"
            }
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    def _generate_template_content(self, platform: str, content_type: str, topic: str) -> Dict[str, Any]:
        """Generate content using templates."""
        templates = self.content_templates.get(platform, {}).get(content_type, [])
        
        if not templates:
            # Use Instagram templates as fallback
            templates = self.content_templates.get("instagram", {}).get(content_type, [
                f"Exploring the fascinating world of {topic}! What's your take?",
                f"Let's dive deep into {topic} - there's so much to discover!",
                f"Sharing some insights about {topic} that might interest you!"
            ])
        
        # Generate 3 suggestions based on templates
        suggestions = []
        selected_templates = random.sample(templates, min(3, len(templates)))
        
        for template in selected_templates:
            suggestion = template.replace("{topic}", topic)
            suggestions.append(suggestion)
        
        return {
            "suggestions": suggestions,
            "platform": platform,
            "content_type": content_type,
            "topic": topic,
            "generated_by": "template"
        }
    
    async def create_content_calendar(self, platform: str, days: int = 7, topics: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate a content calendar for the specified platform."""
        try:
            content_types = ["engagement", "informative", "promotional", "trending"]
            calendar = []
            
            default_topics = ["business", "technology", "lifestyle", "motivation", "tips", "trends", "success"]
            if not topics:
                topics = default_topics
            
            for day in range(1, days + 1):
                # Vary content types throughout the week
                content_type = content_types[(day - 1) % len(content_types)]
                topic = random.choice(topics)
                
                # Generate content for this day
                if self.openai_api_key:
                    try:
                        content_result = await self.get_content_suggestion(platform, content_type, topic)
                        if "suggestions" in content_result and content_result["suggestions"]:
                            suggestion = content_result["suggestions"][0]
                        else:
                            suggestion = f"Create {content_type} content about {topic}"
                    except:
                        suggestion = f"Create {content_type} content about {topic}"
                else:
                    template_result = self._generate_template_content(platform, content_type, topic)
                    suggestion = template_result["suggestions"][0] if template_result["suggestions"] else f"Create {content_type} content about {topic}"
                
                # Optimal posting times by platform
                optimal_times = {
                    "instagram": ["9:00 AM", "2:00 PM", "5:00 PM"],
                    "twitter": ["8:00 AM", "12:00 PM", "3:00 PM", "7:00 PM"],
                    "linkedin": ["8:00 AM", "12:00 PM", "1:00 PM", "5:00 PM"],
                    "facebook": ["9:00 AM", "1:00 PM", "3:00 PM"]
                }
                
                best_time = random.choice(optimal_times.get(platform, ["12:00 PM"]))
                
                calendar.append({
                    "day": day,
                    "content_type": content_type,
                    "topic": topic,
                    "suggested_post": suggestion,
                    "best_time": best_time
                })
            
            return {
                "calendar": calendar,
                "platform": platform,
                "total_days": days,
                "generated_by": "ai" if self.openai_api_key else "template"
            }
            
        except Exception as e:
            return {"error": f"Failed to create content calendar: {str(e)}"}

# Global instance
content_creator = ContentCreator()
