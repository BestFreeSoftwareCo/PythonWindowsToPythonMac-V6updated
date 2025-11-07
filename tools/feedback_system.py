#!/usr/bin/env python3
"""
IRUS V5.0 - Advanced Feedback System
5-star rating system with Discord webhook integration and content filtering
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import time
from datetime import datetime
from tools.discord_integration import DiscordWebhookManager, ContentFilter

class StarRating(ttk.Frame):
    """Interactive 5-star rating widget"""
    
    def __init__(self, parent, callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.callback = callback
        self.rating = 0
        self.stars = []
        
        # Create star buttons
        for i in range(5):
            star_btn = tk.Button(
                self,
                text="☆",
                font=("Arial", 20),
                bg="white",
                fg="gray",
                bd=0,
                cursor="hand2",
                command=lambda idx=i+1: self.set_rating(idx)
            )
            star_btn.pack(side="left", padx=2)
            self.stars.append(star_btn)
            
            # Hover effects
            star_btn.bind("<Enter>", lambda e, idx=i+1: self.hover_rating(idx))
            star_btn.bind("<Leave>", lambda e: self.update_display())
    
    def set_rating(self, rating):
        """Set the rating value"""
        self.rating = rating
        self.update_display()
        if self.callback:
            self.callback(rating)
    
    def hover_rating(self, rating):
        """Show hover effect"""
        for i, star in enumerate(self.stars):
            if i < rating:
                star.config(text="★", fg="#FFD700")  # Gold
            else:
                star.config(text="☆", fg="gray")
    
    def update_display(self):
        """Update star display based on current rating"""
        for i, star in enumerate(self.stars):
            if i < self.rating:
                star.config(text="★", fg="#FFD700")  # Gold
            else:
                star.config(text="☆", fg="gray")
    
    def get_rating(self):
        """Get current rating"""
        return self.rating

class FeedbackWindow:
    """Professional feedback collection window"""
    
    def __init__(self, parent=None):
        self.window = tk.Toplevel(parent) if parent else tk.Tk()
        self.discord_manager = DiscordWebhookManager()
        self.content_filter = ContentFilter()
        
        self.setup_window()
        self.create_interface()
        
    def setup_window(self):
        """Setup feedback window"""
        
        self.window.title("IRUS V5.0 - User Feedback")
        self.window.geometry("600x700")
        self.window.resizable(False, False)
        
        # Center window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.window.winfo_screenheight() // 2) - (700 // 2)
        self.window.geometry(f"600x700+{x}+{y}")
        
        # Configure style
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Submit.TButton', font=('Arial', 11, 'bold'))
    
    def create_interface(self):
        """Create feedback interface"""
        
        # Main container
        main_frame = ttk.Frame(self.window, padding=30)
        main_frame.pack(fill='both', expand=True)
        
        # Header
        header_label = ttk.Label(
            main_frame,
            text="📝 Share Your Experience",
            style='Title.TLabel'
        )
        header_label.pack(pady=(0, 10))
        
        subtitle_label = ttk.Label(
            main_frame,
            text="Help us improve IRUS with your valuable feedback",
            font=('Arial', 10),
            foreground='gray'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Rating section
        rating_frame = ttk.LabelFrame(main_frame, text="Overall Rating", padding=20)
        rating_frame.pack(fill='x', pady=(0, 20))
        
        rating_instruction = ttk.Label(
            rating_frame,
            text="How would you rate your experience with IRUS V5.0?",
            font=('Arial', 10)
        )
        rating_instruction.pack(pady=(0, 15))
        
        # Star rating widget
        self.star_rating = StarRating(rating_frame, callback=self.on_rating_change)
        self.star_rating.pack()
        
        # Rating description
        self.rating_desc = ttk.Label(
            rating_frame,
            text="Click a star to rate",
            font=('Arial', 9),
            foreground='gray'
        )
        self.rating_desc.pack(pady=(10, 0))
        
        # Feedback text section
        feedback_frame = ttk.LabelFrame(main_frame, text="Your Feedback", padding=20)
        feedback_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        feedback_instruction = ttk.Label(
            feedback_frame,
            text="Tell us about your experience (optional):",
            font=('Arial', 10)
        )
        feedback_instruction.pack(anchor='w', pady=(0, 10))
        
        # Text area with scrollbar
        text_frame = ttk.Frame(feedback_frame)
        text_frame.pack(fill='both', expand=True)
        
        self.feedback_text = tk.Text(
            text_frame,
            height=8,
            wrap='word',
            font=('Arial', 10),
            relief='solid',
            borderwidth=1
        )
        
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.feedback_text.yview)
        self.feedback_text.configure(yscrollcommand=scrollbar.set)
        
        self.feedback_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Character counter
        self.char_counter = ttk.Label(
            feedback_frame,
            text="0 / 1000 characters",
            font=('Arial', 8),
            foreground='gray'
        )
        self.char_counter.pack(anchor='e', pady=(5, 0))
        
        # Bind text change event
        self.feedback_text.bind('<KeyRelease>', self.update_char_counter)
        
        # Contact info section
        contact_frame = ttk.LabelFrame(main_frame, text="Contact Information (Optional)", padding=20)
        contact_frame.pack(fill='x', pady=(0, 20))
        
        contact_instruction = ttk.Label(
            contact_frame,
            text="Discord username or email (for follow-up):",
            font=('Arial', 10)
        )
        contact_instruction.pack(anchor='w', pady=(0, 10))
        
        self.contact_var = tk.StringVar()
        contact_entry = ttk.Entry(
            contact_frame,
            textvariable=self.contact_var,
            font=('Arial', 10),
            width=40
        )
        contact_entry.pack(fill='x')
        
        # Privacy notice
        privacy_label = ttk.Label(
            main_frame,
            text="🔒 Your feedback is anonymous and helps improve IRUS for everyone.",
            font=('Arial', 9),
            foreground='gray'
        )
        privacy_label.pack(pady=(0, 20))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x')
        
        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            command=self.window.destroy
        )
        cancel_btn.pack(side='right', padx=(10, 0))
        
        self.submit_btn = ttk.Button(
            button_frame,
            text="Submit Feedback",
            style='Submit.TButton',
            command=self.submit_feedback,
            state='disabled'
        )
        self.submit_btn.pack(side='right')
        
        # Content warning label
        self.warning_label = ttk.Label(
            main_frame,
            text="",
            font=('Arial', 9),
            foreground='red'
        )
        self.warning_label.pack(pady=(10, 0))
    
    def on_rating_change(self, rating):
        """Handle rating change"""
        
        descriptions = {
            1: "⭐ Poor - Needs significant improvement",
            2: "⭐⭐ Fair - Some issues to address", 
            3: "⭐⭐⭐ Good - Generally satisfied",
            4: "⭐⭐⭐⭐ Very Good - Mostly excellent",
            5: "⭐⭐⭐⭐⭐ Excellent - Exceeded expectations"
        }
        
        self.rating_desc.config(text=descriptions.get(rating, "Click a star to rate"))
        
        # Enable submit button if rating is provided
        if rating > 0:
            self.submit_btn.config(state='normal')
        else:
            self.submit_btn.config(state='disabled')
    
    def update_char_counter(self, event=None):
        """Update character counter"""
        
        text = self.feedback_text.get('1.0', 'end-1c')
        char_count = len(text)
        
        self.char_counter.config(text=f"{char_count} / 1000 characters")
        
        # Change color if approaching limit
        if char_count > 900:
            self.char_counter.config(foreground='red')
        elif char_count > 800:
            self.char_counter.config(foreground='orange')
        else:
            self.char_counter.config(foreground='gray')
        
        # Limit text length
        if char_count > 1000:
            self.feedback_text.delete('1.0', f'1.{char_count-1000}')
    
    def validate_content(self):
        """Validate feedback content"""
        
        feedback_text = self.feedback_text.get('1.0', 'end-1c').strip()
        contact_info = self.contact_var.get().strip()
        
        # Check feedback text
        if feedback_text:
            is_clean, violations = self.content_filter.check_content(feedback_text)
            if not is_clean:
                warning = self.content_filter.get_warning_message(violations)
                self.warning_label.config(text=warning)
                return False
        
        # Check contact info
        if contact_info:
            is_clean, violations = self.content_filter.check_content(contact_info)
            if not is_clean:
                warning = self.content_filter.get_warning_message(violations)
                self.warning_label.config(text=warning)
                return False
        
        self.warning_label.config(text="")
        return True
    
    def submit_feedback(self):
        """Submit feedback to Discord"""
        
        # Validate content first
        if not self.validate_content():
            return
        
        rating = self.star_rating.get_rating()
        feedback_text = self.feedback_text.get('1.0', 'end-1c').strip()
        contact_info = self.contact_var.get().strip()
        
        if rating == 0:
            messagebox.showwarning("Rating Required", "Please provide a star rating before submitting.")
            return
        
        # Show loading state
        self.submit_btn.config(text="Submitting...", state='disabled')
        self.window.update()
        
        try:
            # Submit to Discord
            success, message = self.discord_manager.send_feedback(
                rating=rating,
                feedback_text=feedback_text or "No additional feedback provided",
                user_info=contact_info
            )
            
            if success:
                # Show success message
                messagebox.showinfo(
                    "Feedback Submitted",
                    f"Thank you for your {rating}-star feedback!\n\n"
                    "Your input helps us improve IRUS for everyone. "
                    "We appreciate you taking the time to share your experience."
                )
                self.window.destroy()
            else:
                # Show error message
                self.warning_label.config(text=message)
                self.submit_btn.config(text="Submit Feedback", state='normal')
                
        except Exception as e:
            self.warning_label.config(text=f"❌ Submission failed: {str(e)}")
            self.submit_btn.config(text="Submit Feedback", state='normal')

class QuickFeedback:
    """Quick feedback popup for immediate reactions"""
    
    def __init__(self, parent=None, context="general"):
        self.context = context
        self.discord_manager = DiscordWebhookManager()
        
        # Create simple popup
        self.popup = tk.Toplevel(parent) if parent else tk.Tk()
        self.setup_popup()
    
    def setup_popup(self):
        """Setup quick feedback popup"""
        
        self.popup.title("Quick Feedback")
        self.popup.geometry("400x200")
        self.popup.resizable(False, False)
        
        # Center popup
        self.popup.update_idletasks()
        x = (self.popup.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.popup.winfo_screenheight() // 2) - (200 // 2)
        self.popup.geometry(f"400x200+{x}+{y}")
        
        # Content
        main_frame = ttk.Frame(self.popup, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Question
        question_label = ttk.Label(
            main_frame,
            text="How was your experience?",
            font=('Arial', 12, 'bold')
        )
        question_label.pack(pady=(0, 20))
        
        # Quick rating buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack()
        
        ratings = [
            ("😞", 1, "Poor"),
            ("😐", 2, "Fair"), 
            ("🙂", 3, "Good"),
            ("😊", 4, "Very Good"),
            ("🤩", 5, "Excellent")
        ]
        
        for emoji, rating, desc in ratings:
            btn = tk.Button(
                button_frame,
                text=f"{emoji}\n{desc}",
                font=('Arial', 10),
                width=8,
                height=3,
                command=lambda r=rating: self.quick_submit(r)
            )
            btn.pack(side='left', padx=5)
        
        # Detailed feedback option
        detailed_btn = ttk.Button(
            main_frame,
            text="Provide Detailed Feedback",
            command=self.open_detailed_feedback
        )
        detailed_btn.pack(pady=(20, 0))
    
    def quick_submit(self, rating):
        """Submit quick rating"""
        
        context_messages = {
            "conversion": "Conversion process feedback",
            "installation": "Installation experience feedback", 
            "general": "General experience feedback"
        }
        
        feedback_text = context_messages.get(self.context, "Quick feedback")
        
        success, message = self.discord_manager.send_feedback(
            rating=rating,
            feedback_text=feedback_text,
            user_info=f"Quick feedback - {self.context}"
        )
        
        if success:
            messagebox.showinfo("Thank You!", f"Thanks for your {rating}-star feedback!")
        else:
            messagebox.showerror("Error", "Failed to submit feedback. Please try again.")
        
        self.popup.destroy()
    
    def open_detailed_feedback(self):
        """Open detailed feedback window"""
        self.popup.destroy()
        feedback_window = FeedbackWindow()
        feedback_window.window.mainloop()

def show_feedback_window(parent=None):
    """Show main feedback window"""
    feedback_window = FeedbackWindow(parent)
    feedback_window.window.mainloop()

def show_quick_feedback(parent=None, context="general"):
    """Show quick feedback popup"""
    quick_feedback = QuickFeedback(parent, context)
    quick_feedback.popup.mainloop()

if __name__ == "__main__":
    # Test the feedback system
    print("🧪 Testing Feedback System...")
    
    # Test quick feedback
    show_quick_feedback(context="conversion")
    
    # Test detailed feedback
    # show_feedback_window()
